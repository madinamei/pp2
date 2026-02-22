import math

#Built-in Math Functions (min, max, abs, round, pow)
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

x = abs(-7.25)

print(x)

x = pow(4, 3)

print(x)
#math Module Functions (sqrt, ceil, floor, sin, cos, pi, e)
x = math.sqrt(64)

print(x)

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

x = math.pi

print(x)
#random Module (random, randint, choice, shuffle)
import random

num = random.random()
print(num)

num = random.randint(1, 10)
print(num)

colors = ["red", "blue", "green", "yellow"]
picked = random.choice(colors)

print(picked)

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)

print(numbers)

num = random.randrange(0, 20, 2)
print(num)