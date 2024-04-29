#Author: SPC Duong, David                                                                            #
#Date: April 26, 2024                                                                                      #
#Description: This code will hace comments that will explain the code type. #
# Along with answer for the excerise question being asked.                            #
# This code demonstrate the used of print() and input()                                   #
#############################################################


##########################
#  Starting the Lesson                #
##########################

''' If you see this. It multi line comment'''


## 1 
## Try this.
#Parameter: print() and the string "Here we go!"
# Output: the following output from this code will display the phrase: Here we go!
#Explanation: The print() command or function is going to display or output anthing thing that is
# place within the (). In this case it is the string or phrase "Here we go". The reason it is a string is because of
# the quotation marks ""
print("Here we go!")

# Output check: Here we go!


## 1b
## Try this.
# Parameter: print(), str (String) "I can print", str "more than one line"
# Output: The following output from this code will display the phrase: 
# I can print
# more than one line
# Explanation: The print() command or function is going to display or output anthing thing that is
# place within the (). In this case it is the string or phrase "I can print" and "more than one line.". The reason it is a string is because of
# the quotation marks "". The reason for two sentence is that print() was call or type twice, however each time it a different call for print().

# Displaying the phrase: I can print
print("I can print")
#Displaying the phrase: more than one line.
print("more than one line.")


# print("This line won't run because it is 'commented out'. ")
# print("Any line preceded by a '#' will not run.")

## 2a
## Try this.
# Parameter: Print (), Str A phrase
''' Output: If you want
separate lines, you
can also do it 
like this.'''

# Explanation: The \n what allow the phrase to break up into separate line
# when print() is run with the string
print("If you want \n separate lines, you \n can also do it \n like this.")


## 2b
## Try this.
print("This thing inside quotes is called a \"string\". If you want")
print("to put quotes inside of quotes, you precede the quotes with a backslash.")

## 2c
## Try this.
# Explanation: What is happening is the thre quotes (""" '""") is used to type a multi-line string without needing to
# used \n or multiple print() statement
print("""If you put three quote marks, 
you can easily enter a
multi-line
string.""")


## 2d
## You can also use triple quotes similarly to how you use comments:
# Explanation: Another way to  type comment as multiple lines
"""If I wanted to write a long explanation,
I could write it like this
instead of using the '#' if I wanted to."""


## 2e
## Try this.
# Explanation: Allowing the used of  quotes within the string (phrase) being printed by print() statment
print('In Python, the single quote can be used instead of the double quote.')
print("You can put 'single quotes' inside of double quotes, or vice versa, without needing an escape sequence.")
print('However, if you want single quotes inside of single quotes, you\'ll need to escape them using a backslash.')


## 3a
## Try this.
## firstn and lastn are the two variables in this example.
## When you run this, you won't see Smith. Why not?

# Creating a variable or placeholder for  a string called Bob
firstn = "Bob"

# Creating a variable or placeholder for a string called Smith
lastn = "Smith"

# Passing the variable firstn to the print() statement.
# Output: Bob
# Explanation: What was pass to print() is the variable firstn. What is associated with firstn is Bob.
# Smith is not printed because print() online contain firstn not lastn. In order to print Smith. print() must
# contain lastn EX: print(lastn)
print(firstn)


## 3b
## Copy and modify the previous example so that it
## prints firstn, and then prints lastn.

# Creating variable name fname with the value "Bob"
fname = "Bob"

#Creating variable name lname with the value "Smith"
lname = "Smith"

# Passing the created variables to the print() statement
# Output:
# Bob
# Smith
print(fname)
print(lname)




## 4a
## Try this.
## This example uses an f-string. The f stands for "format".
## f-strings are used to insert variables inside of a string.
firstn = "Bob"
lastn = "Smith"
print(f"My name is {firstn} {lastn}")


## 4b
## You can also use commas, but only in functions that
## support it, such as print.
## (Later, when we get to file writing, the 
## comma approach doesn't work, but f-strings do work.)
print("My name is", firstn, lastn)

## (Remember to define your variables.  Where should the variable definitions be placed to be effective?)
