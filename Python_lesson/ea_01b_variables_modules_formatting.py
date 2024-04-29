#Author: SPC Duong, Daivd                                                                        #
#Date: April 27, 2024                                                                                  #
#Description: This code pretain to the less on variable modules formatting#
############################################################

#Importing math library: Allow the user to do arthmetic that not cover by base python

from math import * # The * incidcate that it going to import everythin math library have to offer

## 1
## Ask the user a number.
## Display the number rounded to 3 decimal places.

#Requesting the user to enter a number with 3 decimal places.
"""However a float() conversion function must be place before the input() function is that the
input number will be class as a str (string) type rather than a float (decimal number)"""

usernum = float(input("Please enter a number with 3 decimal places. Press enter when done: "))


#Displaying or output the number enter when prompted.
#Parameter: print(), float usernum
#Output: Float (Decimal) number
""" In order to print or output the number enter by the user, usernum must be pass
to print(). In other words, usernum must be place in between the print( usernum )"""

print(usernum)

## 2 
## Ask the user for the current cost-per-gallon of
## gasoline. Display the cost per pint,
## rounded to the nearest cent.

#Requesting the user to enter the current price for gas
# Using the input() function
""" The price of gas is a decimal number so a float conversion is used on the input statement """
gasprice = float(input("What is the current price of gas? Press enter when done: "))

#Parameter: print(), float gasprice
#Output: User enter gas price
'''' Using the f-string formating print string and the variable gass price.
The .2f is to only print or display 2 signifcant digits if the user enter alot after the
decimal
''''
print(f"$ {gasprice:.2f} per gallon")
