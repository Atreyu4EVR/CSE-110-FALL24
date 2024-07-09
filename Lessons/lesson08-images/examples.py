for i in range(1, 6):
    print(f"i={i}")

x = 25

for i in range(1, 6):
    print(f"i={i}, x={x}")


x = 25

for i in range(1, 6):
    x = x + 1
    print(f"i={i}, x={x}")

print(f"The final value of x is: {x}")

x = 0

for i in range(1, 6):
    x = x + i
    print(f"i={i}, x={x}")

print(f"The final value of x is: {x}")


import random

number = random.randint(1, 10)
print(number)