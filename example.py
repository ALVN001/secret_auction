# from replit import clear
import sys,os
import art
print(art.logo)
dic = {}
print("Welcome to the secret auction program.")
name = input("What is your name?: ")
bid  = int(input("What's your bid?: $"))
dic[name] = bid

print("Are there any other bidders? Type 'yes' or 'no'.")
v = (input()).lower()   
while v!='no':
    os.system('cls')
    name = input("What is your name?: ")
    bid  = int(input("What's your bid?: $"))
    dic[name] = bid
    print("Are there any other bidders? Type 'yes' or 'no'.")
    v = (input()).lower()   

os.system('cls')
max=-1
Hbidder = ""
for key in dic:
    if dic[key]>max:
        max = dic[key]
        Hbidder = key

print(f"The winner is {key} with a bid of ${max}.")