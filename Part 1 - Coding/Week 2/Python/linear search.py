import random

def initialize():
    global list
    print("Welcome to bubble sort algorithm!")
    length = input("How long would you want your list to be?, type RAND for random. (Must be longer than two) \n")
    if length == "RAND":
        list = ["" for _ in range (random.randint(2,20))]
    else:
        list = ["" for _ in range (int(length))]
    print(list)

def filling(list):
    fill = ""
    while fill.upper() != "M" and fill.upper() != "A":
        fill = input("Would you like to fill in the list manually or automatically (Integers only), M/A \n")
    if fill.upper() == "M":
        for i in range(len(list)):
            item = input(f"Input your number for index {i}")
            list[i] = item
    else:
        for i in range(len(list)):
            list[i] = random.randint(0,30)
    print(list)

def linear_search(list):
    print("This is the list", list)
    item = input("What element would you like to obtain the index of? ")
    for i in range(len(list)):
        if str(list[i]) == item:
            return i
    return None





if __name__ =='__main__':
    initialize()
    filling(list)
    i = linear_search(list)
    if i == None:
        print("Item is not in the list.")
    else:
        print("Item is found at: ", i)