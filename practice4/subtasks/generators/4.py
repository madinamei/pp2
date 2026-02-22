a=int(input())
b=int(input())
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

for value in squares(a, b):
    print(value)