# for i in range(1, 6):
#     print(f"i={i}")

# x = 25

# for i in range(1, 6):
#     print(f"i={i}, x={x}")


# x = 25

# for i in range(1, 6):
#     x = x + 1
#     print(f"i={i}, x={x}")

# print(f"The final value of x is: {x}")

# x = 0

# for i in range(1, 6):
#     x = x + i
#     print(f"i={i}, x={x}")

# print(f"The final value of x is: {x}")


# import random

# number = random.randint(1, 10)
# print(number)

# first_name = "Brigham"
# for letter in first_name:
#     print(f"The letter is: {letter}")

# first_name = "Brigham"

# fourth_letter = first_name[3] # Notice, using 3 instead of 4
# print(fourth_letter) # outputs a 'g' on the screen


# first_name = "Brigham"

# for i, letter in enumerate(first_name):
#     print(f"The letter {letter} is at position {i}")

# dog_name = input("What is your dog's name? ")
# letter_count = len(dog_name)

# print(f"Your dog's name has {letter_count} letters")


word = "book"
number_of_letters = 4

for index in range(number_of_letters):
    letter = word[index]
    print(f"Index: {index} Letter: {letter}")