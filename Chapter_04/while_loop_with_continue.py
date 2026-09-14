# This program demonstrates the continue statement with a while loop.
n = 0
while n < 10:
    n += 1
    if n % 3 == 0:
        continue
    print(n)
