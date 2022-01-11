import os
import time

def welcome():  
    print("Hi, whats is your name?")
    time.sleep(2)
    x = str(input("Type your name: "))
    time.sleep(2)
    print("Cool! your name is ", x )
    print("Now let's find out how old are you!")
    time.sleep(2)
    c = int(input("Type your age: "))
    print("Amazing, you are", c)
welcome()

print("Now lets find out where are you from?")
str(input("Type where are you from: "))
