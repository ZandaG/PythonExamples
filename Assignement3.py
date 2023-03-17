"""
Task 1.
Write a Python program to subtract 5 days from the current date.
"""
from datetime import date, timedelta
dt = date.today() - timedelta(5)
print("Today is:",date.today())
print("5 days before today is:",dt)

"""
Task 2.
Write a program to print out all the numbers from 0 to 100 that are divisible by 7.
"""
for i in range(0,100+1):
    if(i%7==0):
        print(i)
"""
Task 2.
Write a program in Python to reverse a word. Words should be provided using input function.
"""

username = input("Enter username:")
username2 = reversed (username)
for x in username2:
    print(x)



