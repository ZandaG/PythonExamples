"""
1. Create an input screen where the user should specify –
the name, surname and personal ID number.
2. Entered user information is required to save in a text file,
which will be created under a folder with the following name
– YYYY-MM-dd(Every day, a new folder with the date name and text file will be created).
3. The text file name contains the ID number.
A new text file is created for every unique ID number in today’s date folder.
"""
import os

if not os.path.exists("User_Info"):
    os.makedirs("User_Info")

file_name = "userid.txt"
with open (file_name, "w", encoding="utf-8") as user_file:
    user_file.write (input ("What is you name?:"))
    user_file.write ("\n")
    user_file.write (input ("What is you surname?:"))
    user_file.write ("\n")
    user_file.write (input ("Please provide your ID number:"))

with open("userid.txt") as f:
    contents = f.readlines()
