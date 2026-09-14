# This program demonstrates the break statement with a while loop.
n = 0
while n < 100:
    print(n)
    if n == 5:
        break
    n += 1

print(f'The loop stopped and n is {n}.')