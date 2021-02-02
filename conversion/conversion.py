'''
Created on Jan 20, 2021

The objective is to make a program that can complete different conversions

'''

#Use input() to get the number of miles from the user. ANd store 
#that int in a variable called miles.

miles = input("How many miles would you like to convert?")

#Convert miles to yards, using the following: 
#1 mile = 1760
#Store the value in a variable called yards and print it our with a 
#simple statement.

yards = miles * 1760 
print(str(miles)) + "convert to" + str(yards) + "yards."

#conver miles to feet, using the following 
# 1 mile = 5280 feet.
#Store the balue in a variable called feet and print it our with a 
#simple statement

feet = miles * 5280
print(str(miles)) + "convert to" + str(feet) + "feet."

#conver miles to inches, using the following:
#1 mile = 63,360 feet 
#Store the value in a variable called inches and print it our with a 
#simple statement.

inches = miles * 63360
print(str(miles)) + "convert to" + str(inches) + "inches."

