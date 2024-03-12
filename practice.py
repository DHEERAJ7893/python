# print("Welcome to coding Quiz")

# playing=input('do you want paly:')

# if playing != "yes":
#     quit()
    
# print("start the game:)")
    
# question =input("a means?")
# if question == "apple":
#     print("correct")
# else:
#     print("incorrect!")
    
# question =input("b means?")
# if question == "bannana":
#     print("correct")
# else:
#     print("incorrect!")
    
# question =input("c means?")
# if question == "cat":
#     print("correct")
# else:
#     print("incorrect!")

# question =input("d means?")
# if question == "dog":
#     print("correct")
# else:
#     print("incorrect!")
    
# question =input("e means?")
# if question == "egg":
#     print("correct")
# else:
#     print("incorrect!")
    
# question =input("f means?")
# if question == "fish":
#     print("correct")
# else:
#     print("incorrect!")
    
# question =input("g means?")
# if question == "goat":
#     print("correct")
# else:
#     print("incorrect!")
    
# question =input("h means?")
# if question == "hat":
#     print("correct")
# else:
#     print("incorrect!")
    
# maths = int(input("add the two numbers 1+2 ?"))
# if maths == 3:
#     print("corret")
# else:
#     print("incorrect!")
    
# import random

# action = input("enter a choice(rock,paper,scissors):")
# # possible = ["rock","paper","scissors"]
# # computer = random.choice(possible)
# user = input("enter a choice(rock,paper,scissors):")
# print(f"\nyou choose {action} user2 chose {user}.\n")
# if action == user:
#     print(f"both players selected {action}. it's a tie!")
# elif action == "rock":
#     if user == "scissors":
#         print("rock smashes scissors! you win!")
#     else:
#         print("paper covers rocks! you lose!")
# elif action == "paper":
#     if user == "rock":
#         print("paper covers rocks! you won!")
#     else:
#         print("scissors cuts paper! you lose!")
# elif action == "scissors":
#     if user == "paper":
#         print("scissors cuts paper! you won!")
#     else:
#         print("rock smashes scissors! you lose!")

# x = 36/4*(3 + 2)* 4 + 2 
# print(x)

# salary = 8000
# def my_salary ():
#     salary = 12000
#     print("salary: ", salary)
# my_salary()
# print("salary: ", salary)

# def calculate(num1 ,num2=4):
#     res = num1 * num2
#     print(res)
# calculate(4, 6)

# name = "pynative"
# print(name[1:3])

# for i in range(10, 15, 1):
#     print(i, end=' ,')
# else:
#     print("happy ending")


# var = "james bond"
# print(var[2::-1])

# sampletest ={'vicky','kamal','sai'}
# sampletest.add('vickydd')
# print(sampletest)

# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000.
# Otherwise, return their sum.

# def multiplication(num1, num2):
#     multiplic = num1 * num2
#     if multiplic <= 1000:
#         return multiplic
#     else:
#         return num1 + num2

# result = multiplication(200 ,100)
# print(result)
# result = multiplication(40 ,60)
# print(result)
# a = 'python'
# list = ['database','python','react']
# if (a not in list):
#     print('python')
# else:
#     print('database')


# game = 'cricket'
# game = 'footbal'
# if game == 'cricket':
#     print('kohli is a player')
#     print('dhoni is a player')
# elif game == 'footbal':
#     print('sachin is a player')
# else:
#     print('its not a cricket')

# num = 10
# if num >= 10:
#     if num == 10:
#         print("zero")
#     else:
#         print("positive number")
# else:
#     print("negative number")

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("enter the amount? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                ("amount is greater than zero")
        else:
            print("please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("enter the number of lines to ben on (1-"+ str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter a valid number of lines")
        else:
            print("please enter a number")
    return lines

def get_bet():
     while True:
        amount = input("enter the number of lines to bet ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET :
                break
            else:
                (f"amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("please enter a number")
            return amount
    
def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet
    print(balance,lines,bet)
    
main()