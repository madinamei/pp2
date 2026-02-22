#iternext
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

t = (1, 2, 3)
it = iter(t)

print(next(it)) 
print(next(it))

r = range(3)
it = iter(r)

print(next(it)) 
print(next(it))  

#looping through an iterator

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

mystr = "banana"

for x in mystr:
  print(x)

numbers = [1, 2, 3]
it = iter(numbers)

for num in it:
    print(num)

numbers = [4, 5, 6]
it = iter(numbers)

while True:
    try:
        print(next(it))
    except StopIteration:
        break

it = iter("Hello")

for letter in it:
    print(letter)
#create an iterator
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class Even:
    def __init__(self, max):
        self.max = max
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 2
        if self.num <= self.max:
            return self.num
        else:
            raise StopIteration

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 0:
            value = self.current
            self.current -= 1
            return value
        else:
            raise StopIteration

#yield keywords

def my_gen():
    yield 1
    yield 2
    yield 3

g = my_gen()

print(next(g))
print(next(g))

def count_up(n):
    for i in range(1, n + 1):
        yield i

for num in count_up(5):
    print(num)

def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

#generator func
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def reverse(text):
    for i in range(len(text)-1, -1, -1):
        yield text[i]

def positives(numbers):
    for num in numbers:
        if num > 0:
            yield num

def words(sentence):
    for word in sentence.split():
        yield word

def multiples(n, limit):
    for i in range(limit):
        yield i * n

#generator expressions
gen = (x for x in range(5))

for num in gen:
    print(num)

gen = (x**2 for x in range(5))

gen = (x for x in range(10) if x % 2 == 0)

words = ["apple", "banana", "cherry"]
gen = (len(word) for word in words)