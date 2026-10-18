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
        fill = input("Would you like to fill in the list manually or automatically, M/A \n")
    if fill.upper() == "M":
        for i in range(len(list)):
            num = int(input(f"Input your number for index {i}"))
            list[i] = num
    else:
        for i in range(len(list)):
            list[i] = random.randint(0,30)
    print(list)

def sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            while list[j] > list[j+1]:
                temp = list[j+1]
                list[j+1] = list[j]
                list[j] = temp
    print(list)

def search(list):
    start = 0
    end = len(list)-1
    print("The current list is: ", list)
    item = int(input("Input the item you want to search for: "))
    middle = (start+end) // 2
    while start != end and start <= end:
        print("Top", start)
        print("End", end)
        print("Middle", middle)
        if item == list[middle]:
            return middle
        elif list[middle] > item:
            end = middle
            middle = (start+end) // 2
        elif list[middle] < item:
            start = middle
            middle = (start+end) // 2
    return None


if __name__ =='__main__':
    initialize()
    filling(list)
    sort(list)
    i = search(list)
    if i == None:
        print("Your item is not in the list.")
    else:
        print("Your item is at: ", i)