def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it.
    '''
    global cur_temp # in degrees Celsius
    global cur_charge # in percentage 
    global cur_time # in minutes

    global good_battery_health
    cur_charge = 50
    cur_temp = 20
    cur_time = 0
    good_battery_health = True
    global overcharge_occur
    overcharge_occur = 0

def simulate_activity(activity, duration):
    global cur_time,cur_charge,cur_temp,good_battery_health,overcharge_occur
    Flagged_over = False # used to detect whether it was flagged as overcharge in a single activity
    if activity == "charge":
            while duration > 0:
                cur_time = cur_time + min(1,duration)
                min_used = min(1,duration)
                if cur_charge >= 100:
                    cur_temp = cur_temp + (0.25 * min_used)
                elif good_battery_health and cur_charge < 80 and cur_temp < 40:
                    time_fast_avail = min(1,duration_fast_charge_possible())
                    time_slow = min_used - time_fast_avail
                    cur_charge = (cur_charge + (3*time_fast_avail))
                    cur_temp = cur_temp + (0.5*time_fast_avail)
                    cur_charge = (cur_charge + (1*time_slow))
                    cur_temp = cur_temp + (0.25*time_slow)
                elif good_battery_health and cur_charge >= 80 or cur_temp >= 40 and good_battery_health:
                    cur_temp = cur_temp + (0.25*min_used)
                    cur_charge = min(100,(cur_charge + (1*min_used)))
                elif good_battery_health == False and cur_charge < 80:
                    cur_temp = cur_temp + (0.25*min_used)
                    cur_charge = min(80,(cur_charge + (1*min_used)))
                else:
                    cur_temp = cur_temp + (0.25*min_used) 
                if cur_time > 360:
                    cur_time = 0
                if cur_charge >= 90 and Flagged_over == False:
                    overcharge_occur = overcharge_occur + 1
                    Flagged_over = True
                if overcharge_occur == 3:
                    good_battery_health = False
                duration = duration - min(1,duration)
            if cur_time > 360:
                cur_time = 0
    elif activity == "use":
        while duration > 0:
            cur_time = cur_time + min(1,duration)
            min_used = min(1,duration)
            if cur_time > 360:
                cur_time = 0
            if cur_charge == 0:
                if cur_temp - (1*min_used) > 0:   # checking if temp would be negative when subtracted
                    cur_temp = cur_temp - (1*min_used) # temp would decrease by 1 every 1 minute
                else:
                    cur_temp = 0
            else:
                if cur_charge - (2*min_used) < 0: # checking if charge would be negative when subtracted
                    active_time = cur_charge / 2.0  # if - , then there would be active time left and dead time
                    dead_time = min_used - active_time
                    cur_charge = 0.0 # dead
                    cur_temp = cur_temp + (1 * active_time) - (1 * dead_time) # temp raised and decreased
                    if cur_temp < 0:
                        cur_temp = 0.0
                else:
                    cur_charge = cur_charge - (2*min_used)
                    cur_temp = cur_temp + (1*min_used)
            duration = duration - min(1,duration)
    elif activity == "idle":
        while duration > 0:
            cur_time = cur_time + min(1,duration)
            min_used = min(1,duration)            
            if cur_time > 360:
                cur_time = 0
            if cur_charge - (0.5*min_used) > 0: # checking if the next calculation results in - value
                cur_charge = cur_charge - (0.5*min_used)
            else:
                cur_charge = 0
            if cur_temp - (1*min_used) > 0:
                cur_temp = cur_temp - (1*min_used)
            else:
                cur_temp = 0
            duration = duration - min(1,duration)
    else:
        pass

def duration_fast_charge_possible():
    if cur_charge >= 80 or cur_temp >= 40:
        return 0
    elif good_battery_health == False:
        return 0
    else:
        starting_charge = cur_charge
        starting_temp = cur_temp
        mins = 0
        while starting_charge < 80 and starting_temp < 40:
            if (starting_charge + 3) <= 80 and (starting_temp + 0.5) <= 40: # if full cycle of 1 minute permits to do so
                starting_charge = starting_charge + 3
                starting_temp = starting_temp + 0.5
                mins = mins + 1
            else:
                charge_left = 80 - starting_charge # charge left available in fast
                temp_left = 40 - starting_temp # temp left avaliable in fast
                full_charge_cycle = charge_left/3 
                full_temp_cycle = temp_left/0.5
                if full_charge_cycle > full_temp_cycle: # comparing the amount of fast charge permitted
                    mins = mins + full_temp_cycle 
                else:
                    mins = mins + full_charge_cycle
                return mins 
        return mins 
def get_cur_temp():
    return cur_temp

def get_cur_charge():
    return cur_charge

def get_cur_battery_health():
    return good_battery_health

def charge_time_needed(minutes):
    charge = cur_charge
    temp = cur_temp
    if (minutes*2) > 100:
        return None
    elif (charge/2) >= minutes:
        return 0
    else:
        charge_needed = minutes*2
        time_needed = 0
        while charge_needed > charge:
            charge_left = min(1,(charge_needed - charge)) # % requird, increments of 1
            if charge_needed > 80 and not(good_battery_health):
                return None
            if charge < 80 and temp < 40 and good_battery_health:
                time_added = charge_left / 3.0
                if (charge_left + charge) <= 80 and (temp + charge_left * 0.5) <= 40: # if the increment fully stays in fast charge
                    charge = charge_left + charge
                    temp = temp + (time_added * 0.5)
                    time_needed = time_needed + time_added
                else:
                    fast_cap = min(80 - charge, ((40 - temp) / 0.5) * 3) # which one reaches first, temp or charge , temp can determine the amount of charges permitted, as 0.5 temp = 3%
                    fast_time = fast_cap / 3.0 # 3 full charge needs 1 minute
                    charge = charge + fast_cap 
                    temp = temp + (fast_time * 0.5) # 0.5 degrees celcius goes up every 1 minute
                    time_needed = time_needed + fast_time                         
            elif charge >= 80 or temp >= 40 or (not(good_battery_health) and charge < 80):
                charge_used = min(1, charge_left)
                time_added = charge_used        # 1% charge = 1 minute    
                temp = temp + (0.25 * time_added) # 1 minute = 0.25 degrees celcius
                charge = charge + charge_used
                time_needed = time_needed + time_added
        return time_needed
if __name__ == '__main__':
    initialize()
    print(duration_fast_charge_possible()) # 10
    print(charge_time_needed(50)) # 30

    simulate_activity("charge",30)
    print(get_cur_charge()) # 100
    print(get_cur_temp()) # 30

    simulate_activity("use",50)
    print(get_cur_charge()) # 0
    print(get_cur_temp()) # 80

    simulate_activity("use",10)
    print(get_cur_charge()) # 0
    print(get_cur_temp()) # 70

    simulate_activity("charge",100)
    print(get_cur_charge()) # 100
    print(get_cur_temp()) # 95

    simulate_activity("idle",100)
    print(get_cur_charge()) # 50
    print(get_cur_temp()) # 0
    print(get_cur_battery_health()) # True
    print(duration_fast_charge_possible()) # 10

    simulate_activity("charge",80)
    print(get_cur_charge()) # 90
    print(get_cur_temp()) # 22.5
    print(get_cur_battery_health()) # False

    simulate_activity("use",40)
    print(get_cur_charge()) # 10
    print(get_cur_temp()) # 62.5

    simulate_activity("charge",80)
    print(get_cur_charge()) # 80
    print(get_cur_temp()) # 82.5

    initialize()
    cur_charge = 78
    print(duration_fast_charge_possible()) # 0.666666
#     # add your tests here

    initialize()
    simulate_activity("charge",290)
    print(get_cur_charge())
    simulate_activity("idle",30)
    print(get_cur_charge())
    simulate_activity("charge",10)
    print(get_cur_charge())
    simulate_activity("idle",20)
    print(get_cur_charge())
    simulate_activity("charge",10)
    print(get_cur_charge())
    print(get_cur_battery_health())
