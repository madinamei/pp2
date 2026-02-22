n=int(input())
def squares(n):
    for i in range(n + 1):
        yield i * i

for num in squares(n):
    print(num)