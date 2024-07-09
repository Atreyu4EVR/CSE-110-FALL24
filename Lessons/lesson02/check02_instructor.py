"""
File: check02_instructor.py
Author: Brother Burton

Purpose: Display text to the screen.
"""

first = input("What is your first name? ")
last = input("What is your last name? ")

print(f"Your name is {last}, {first} {last}.")

# Be aware that there are many ways to do the formatting of that line, such as:
# print("Your name is " + last + ", " + first + " " + last + ".")
# print("Your name is {}, {} {}.".format(last, first, last))
# print("Your name is {0}, {1} {0}.".format(last, first))
