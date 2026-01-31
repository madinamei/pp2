print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a1)

a = "Hello"
print(a)

b = "Hello, World!"
print(b[2:5])

a2 = "Hello, World!"
print(a2[:5])

c = "Hello, World!"
print(c[2:])

d = "Hello, World!"
print(d[-5:-2])

f = "Hello, World!"
print(a.upper())

f2 = "Hello, World!"
print(a2.lower())

f3 = " Hello, World! "
print(a3.strip()) # returns "Hello, World!"

k = "Hello, World!"
print(k.split(",")) # returns ['Hello', ' World!']


x = "Hello"
y = "World"
z = x + y
print(z)

x2 = "Hello"
y2 = "World"
z2 = x2 + " " + y2
print(z2)


age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price2 = 59
txt2 = f"The price is {price2:.2f} dollars"
print(txt2)

txt3 = f"The price is {20 * 59} dollars"
print(txt3)

txt4 = "We are the so-called \"Vikings\" from the north."
print(txt4)