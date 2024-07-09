people = [
    "Stephanie 36",
    "Wesley 32",
    "Levi 93",
    "Gretchen 54",
    "Noah 500",
    "Penelope 32",
    "Methuselah 969",
    "Sarah 101"
]

# Start our youngest_age variable at something larger than anyone we'll find
oldest_age = -4

# This will keep track of the person with the youngest age
oldest_name = ""

# Go through each person in the list
for person_line in people:

    parts = person_line.split() # by default this will split on the space

    # Set variables for the two different parts
    name = parts[0]
    age = int(parts[1])

    # Check to see if this current person is younger than the youngest
    # that we have seen so far
    if age >= oldest_age:
        # This person is the new "youngest"

        # Save their age as the new youngest
        oldest_age = age

        # Save their name as the youngest name
        oldest_name = name

# Outside of the loop, so we are all done now
print(f"Wow, the oldest prophet was {oldest_name} with an age of {oldest_age}")