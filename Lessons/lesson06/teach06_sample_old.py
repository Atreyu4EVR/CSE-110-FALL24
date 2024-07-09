"""
File: teach06_sample.py
Author: Brother Burton

Purpose: Amusement park ride requirements.
"""
# Notice the use of a boolean variable, set to False by default
can_ride = False

age1 = int(input("What is the age of the first rider? "))
height1 = int(input("What is the height of the first rider? "))

is_second_rider = input("Is there a second rider (yes/no)? ")

if is_second_rider.lower() == "yes":
    age2 = int(input("What is the age of the second rider? "))
    height2 = int(input("What is the height of the second rider? "))

    # Rule 1
    if height1 < 36 or height2 < 36:
        can_ride = False
    else:
        if age1 >= 12 and age2 >= 12:
            # Rule 3
            if height1 >= 48 and height2 >= 48:
                # They are both over 12 years and 48 inches
                can_ride = True

            # Rule 6
            if age1 >= 18 and age2 >= 18:
                # Two adults are good to go!
                can_ride = True

            # Rule 7
            if height1 >= 36 and (height2 >= 60 or age2 >= 18):
                # The first is small but the second is 18 years or 60 inches
                can_ride = True
            elif height2 >= 36 and (height1 >= 60 or age1 >=18):
                # The second is small but the first is 18 years or 60 inches
                can_ride = True
            
        else:
            # One of these riders is less than 12, and at this point we are only
            # handling the cases for people 12 and older so we will say no to
            # these people. Come back and ride later!
            can_ride = False

else: # this means its a single rider
    # Rule 2
    if age1 >= 18 and height1 >= 68:
        can_ride = True
    else:
        can_ride = False


if can_ride:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")
