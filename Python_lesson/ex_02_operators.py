#Author: SPC Duong,David                                                      #
#Date: April 27,2024                                                                #
# Description: Code pretain to the excreises on 2b operators   #
##################################################


## 2
## Now let's incorporate some inputs.
## Ask the user for two numbers.
## Display "If you divided ___ by ___, then you
## would get ____ with a remainder of ___".

input1 = int(input(" Please enter a number. Press enter when done: "))
input2 = int(input(" Please enter a second number. Press enter when done: "))

math_cal = input1 / input2
remainder_cal = input1 % input2

print(f' Ifyou divided {input1} by {input2}, \n then you would get {math_cal} \n
      ' with a remainder of {remaider_cal}')


## 3
## Calculating an exponent
## Ask the user for two numbers.
## Display "If you computed ___ to the power of ___, then you would get ___."
## (Hint: What is the operator for exponent in Python?
##  It may not be what you think.)

num1 = int(input("Please enter a number. Press enter when done: "))
num2 = int(input("Please enter a second number. Press enter when done. "))

expo_cal = num1 ** num2

print(f"If you computed {num1} to the power of {num2}, then you would get {expo_cal} ")



