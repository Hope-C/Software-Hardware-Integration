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
if __name__ =='__main__':
    initialize()
    filling(list)
    sort(list)