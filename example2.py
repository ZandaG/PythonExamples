
#Input funkcija

x = input ("Enter the file name:")
print ("Output:" + x)

# if - else statement
i = 5
if i > 15:
      print ("10 is less than 15")
else:
   print ("Not true")

#  short version of if-else
a = 400
b = 300
print ("A") if a > b else print("B")

# match statements

lang = input ("Which programming language you want to learn?")
match lang:
  case "JavaScript":
    print ("You can become a web developer")
  case "Python":
    print ("You can become a Data Scientist")
  case "Java":
    print ("You can become a mobile app developer")
  case _:
    print ("It does not matter")

# LISTS

thislist = ["apple", "banana", "cherry"]
       #      0         1         2
thislist[0] = "kivi"
print(thislist)

# copy list
thislist = ["apple", "banana", "cherry"]
thislist2 = thislist
print(thislist)
print(thislist2)

# atdalitas listes

thislist = ["apple", "banana", "cherry"]
thislist2 = thislist.copy()
thislist[0] = "kivi"
print(thislist)
print(thislist2)

# tuple - cannot be changed

