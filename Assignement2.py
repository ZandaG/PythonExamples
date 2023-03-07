
"""
Task 1.
 Write a small program that assigns the name of 2 items to 2 variables.
 If the values of the 2 variables are equal,
 print the message"The items are the same".
 Otherwise, print"The items are different"
"""

x= "Monday"
y= "Friday"

if x == y:
      print("The items are the same")

else:
    print("The items are different")



"""
Task 2.
Write a program to ask for a name and an age.
When both values have been entered, check if the person is 18 to enter the club. If yes, welcom, if not,print polite 
"""

name = input ("What is you name?:")
age = int (input ("How old are you?:"))

if age >= 18:
    print ("You are welcome!")
else:
    print("Sorry, you are not allowed to enter!")