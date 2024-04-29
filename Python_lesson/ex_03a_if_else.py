'''
Author: SPC Duong, David
Date: April 27, 2024
Description: The following code pretain to the excerise for if-else statement
'''
#Improting everything from the random library
import random

## 1b
## Copy and modify the above example so that the computer will 
## pick numbers between 1 and 4 instead.

#creating a variable that randomly generate a number between 1 and 4

# randnum = random.randint(1,4)

# displaying the random generated number
# print(f"Here's a random integer : {randnum}")

## 1e
## Copy and modify the previous example so that if the randomly
## chosen number is 10, it will say "Wow, a two digit number!"

#creating a variable that generated a number between 0-10
# doublenum = random.randint(0,10)

#outputtin the generated number 
# print(f"Here's a random integer : {doublenum}")

#Using a conditional statement to print out a statement if the number is 10

# if doublenum == 10: # If the conditional statement (doublenum equal 10) the statement will print
    # print("Wow, a two digit number! ")
    

## 3
## Copy and modify the above example so that "dell" is one of the names
## that can be randomly chosen.


# listname = random.choice(["bob", "susan", "joe", "anna", "dell"])
# print(f"Hey {listname}.") 
# if listname == "joe":
#     print("Your name rhymes with low.")



## 3b
## Copy and modify the above example so that 
## if the name is "dell", it will print "That’s a computer brand."

#variable: namelist: a list of names for the random generater to pick from
# namelist = random.choice(['bob', 'susan', 'joe', 'anna', 'dell'])

#display the generated name
# print(f'Hey {namelist}. ')

#creating a conditional statement.
# if the statement is true. Output a string
# if namelist == 'dell': # need to have two equal for comparing
#     print(f"{namelist}. That’s a computer brand.")

## 3c
## Try this.
## Notice that the "Have a good day" line prints regardless of
## the chosen name.  This is because it is
## not indented (it has no spaces before the line).
# import random
# name = random.choice(["bob", "susan", "joe", "anna"])
# print(f"Hey {name}.") 
# if name == "joe":
#     print("Hello Joe!")
#     print("Your name rhymes with low.")
    
# '''The reason is the print statement is not within the if statement. It is outside the if statement.'''
# print("Have a good day.") 


## 5
## Copy and modify the above example so that the
## legal drinking age is 40. (Just to be funny.)

#variable: userage; will generate a random integer between 18-50
# userage = random.randint(18,50)


#Output the genernation age using a f-string print() statement
# print(f'Pretend that you are {userage} years old. ')

#creating a conditional statement (if-else). If it true it will output
#a statement. Otherwise it will output something else
# if userage < 40:
#     print("you can't drink alcohol in the US yet. SUCK TO SUCK =P")
# else:
#     print("Congratulation you can drink. Drink responsibly 😊 or not 🤷")

## 6b
## Change the previous example so that if the
## user types "bob", it will reply "Are you the painter?"

#Variable:  str(string) nameinpt; requesting a name(string) from the user
# The input() statement allow the user to enter a name
# nameinpt = input("Please enter a name: Press enter when done: ")

#Variable: str string1; assign the string 'bob
# string1 = 'bob'
# creating a conditional statement. True: print a statement otherwise print a Hello statement
# Comparing the two variable without worrying about uppercase or lowercase
# if nameinpt.casefold() == string1.casefold(): #casefold() take the string from nameinpt and string1 and compare it without caring if it Upper or lowercase
#     print(f"{nameinpt}! Are you the painter?")
# else:
#     print(f"Hello {nameinpt}.")

#actual class answer
# if nameinpt == 'bob': 
#     print(f"{nameinpt}! Are you the painter?")
# else:
#     print(f"Hello {nameinpt}.")

## 7
## Modify the above example so that if the name is
## "Pluto", it will say "Is it a planet or not?" 

#Variable: str laname; request user for a name
# str findplu; assign the value 'Pluto'
# laname = input("Please enter a name. Press enter when done: ")

# findplu = 'Pluto'
# pluPlu = findplu.casefold() # assigning findplu with casefold() to pluPlu

#Conditional statement
# if laname.casefold()== pluPlu:
#     print(f'{laname}. Is it a planet or not')
# else:
#     print(f"Hello {laname}")

# Actual class answer
# if laname == "Pluto":
#     print(f"{laname}. Is it a planet or not")
# else:
#      print(f"Hello {laname}")

## 7bb
## Copy and modify the previous example so that
## if the name is "Ruby", it displays
## "That name is also the name of a gem."
## Make it work for any capitalization of Ruby.
########################
##  INSTRUCTOR-CHECK  ##
########################

#Variable: str userinpt; assign the input value from user
#requesting a name from the user
# userinpt = input("Please enter a name. Press enter when done:")

# #Variable: rubyname; Assign the value "Ruby"

# rubyname = 'Ruby'

# #Variable: ruru; assign the value of rubyname without consideration of upper or lowercase
# ruru = rubyname.casefold()

# #Conditional statement
# if userinpt.casefold() == ruru:
#     print(f'{userinpt}. That name is also the name of a gem')
# else:
#     print(f'Hello. {userinpt}')

# #Actual class answer

# if userinpt.lower() == 'ruby':
#     print(f'{userinpt}. That name is also the name of a gem')
# else:
#     print(f'Hello {userinpt}. ')

## 7d
## - Ask the user for a name
## - If the name is anything other than Bob, then
##   display "I don't think I know you. I only know Bob."
## Hint: the != operator means "not equal".

#Variable: string requestnme; request a name from user. The variable will contain a string value
# requestnme = input("Please enter a name. Press enter when done: ")


#Conditional state me

# if requestnme.lower() != 'bob':
#     print(f"{requestnme}. I don't think I know you. I only know Bob")
# else:
#     print(f'Greeting {requestnme}.')

## 7dd
## - Ask the user for a number
## - If the number is not equal to 5, say "You should have picked 5." 
## (Use the != operator)

#converting the input from string to int.
#Don't have to. But make sure it the 5 is a string
# numnum = int(input("Please enter a number. Press enter when done: "))

# numnum != '5' if input is a string value
# if numnum != 5:
#     print("You should of have picked 5")
# else:
#     print(f"{numnum}. Are you a mind reader?")

## 7e
## - Ask the user for a name
## - If the name is empty, say "You didn't type anything!"
## - Otherwise, say "Hi ___."
## Hint: an empty name would be quotes with nothing inside, so
##     you might use something similar to this piece of code:
##     if whatTheUserTyped == "":
##           print("Something would go here.")

# blanknam = input('Please enter a name. Press enter when done')

# if blanknam == "":
#     print("You didn't type anything! Learn to read")
# else:
#     print(f'Hi {blanknam}.')

## 8 
## Try this. 
# age = 10 
# ageNextYear = age + 1 
# print(ageNextYear) 
     

# ## 9
# ## Try this. Note: you will get an error. 
# age = input("How old are you?") 
# ageNextYear = age + 1 
# print(ageNextYear) 
     

# ## 10 
# ## Try this. 
# age = int(input("How old are you?")) 
# ageNextYear = age + 1 
# print(ageNextYear) 

#Answer: When you are doing arithmetic you must convert the input to a int or float
# The input take whatever value enter as a string.

## 11
## Copy and modify the previous example to do the following: 
## - Ask the user for age 
## - Say "I see you are __ years old.
##        You will be 65 years old in __ years."
##   For example, if the user typed 45, then it would display
##      "I see you are 45 years old.
##       You will be 65 years old in 20 years."
########################
##  INSTRUCTOR-CHECK  ##
########################

#Requesting for an age from the user
# agerequest = int(input("Please enter an age. Press enter when done: "))

# # Preforming calculation
# # determining when the person will be 65
# simcal = 65 - agerequest

# #Output a statement with the calculation and age enter by user
# print(f'I see you are {agerequest} years old\nYou will be 65 years old in {simcal} years')

## 13
## Modify the above example so it works.
## You’ll use the `int` function. 


# age = int(input("How old are you?"))
# if age < 21: 
#     print("You can't drink alcohol in the US yet.") 
# else: 
#     print("You are legally allowed to drink. Drink responsibly 😊 ") 

# The answer ^ LOL
# or try this

# age = input("How old are you?") 
# if age < '21': 
#     print("You can't drink alcohol in the US yet.") 
# else: 
#     print("You are legally allowed to drink. Drink responsibly 😊 ") 

## 14
## Copy and modify the above example so that
## it shows how many years remain until you can
## drink (but only display that if you’re
## under the drinking age). 

# age = int(input("How old are you?"))

# if age < 21: 
#     legalage = 21 - age
#     print(f"You are legall allow to drink in {legalage} years") 
# else: 
#     print("You are legally allowed to drink. Drink responsibly 😊 ") 
     

## 15
## Write a program that takes a name from the user.
## If the name is the letter "A", say
## "Your name is just the letter A? That’s kinda cool".
## Otherwise, say "Ok, your name is ___".    

# namnam = input("Please enter your name. Press enter when done: ")

# if namnam == "A":
#     print(f"{namnam}. Your name is just the letter A? That's kinda cool")
# else:
#     print(f"Ok, your name is {namnam}")


## 17c
## Copy and modify the previous example so that each `elif` is
## simply `if`. How does it act differently? 

# heightInInches = int(input("Give me a number: "))
# if heightInInches < 0:
#     print("You can't have a negative height!")
# if heightInInches <= 55:
#     print("That's relatively short.")
# if heightInInches <= 72:
#     print("That's around average.")
# else:
#     print("That's pretty tall.")

#HeightInIches value get compared to all three if statement

## 18
## Ask the user how many French fries they want.
## Display different responses depending on how many they
## request. (Examples: "That’s way too many!", etc.

ffamount = int(input("How many French fries do you want? Press enter when done: "))
if ffamount < 0:
    print("Good choice French Fries is not good for you")
elif ffamount <= 2:
    print("That a small amount")
elif ffamount <=10:
    print("That's way too many! Fries")
else:
    print("Sorry that way too much Fries. I'm not making that much")


