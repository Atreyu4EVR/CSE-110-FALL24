cars = 3
people = 8

people_per_car = people / cars

# Round to 1 decimal
print(f"There are {people_per_car:.1f} people in each car.")

# Round to 2 decimals
print(f"There are {people_per_car:.2f} people in each car.")

# Round to 3 decimals
print(f"There are {people_per_car:.3f} people in each car.")

#########

distance = 9 * 1205 * 18

# Scientific notation with 3 digits of precision
print(f"The distance is: {distance:.3e} meters.")
# Output:

# Scientific notation with 6 digits of precision
print(f"The distance is: {distance:.6e} meters.")
# Output:

##########

big_number = 123456789

# Display without formatting:
print(f"The number is: {big_number}")
# Output:

# Display with "," formatting:
print(f"The number is: {big_number:,}")
# Output:

# Display with "_" formatting:
print(f"The number is: {big_number:_}")
# Output:

############

import math

radius = 5
area = math.pi * (radius ** 2)
print(f"The area is: {area}")

#########
value = 1.23456789

print(value)

rounded_value = round(value, 2)

print(rounded_value)

###########
import math

weight = 1.65

lower = math.floor(weight)
print(lower)
# Output: 1

higher = math.ceil(weight)
print(higher)
# Output: 2
