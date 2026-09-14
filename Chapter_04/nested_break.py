# This program demonstrates the break statement
# inside a nested inner loop.
for outer in range(5):
    for inner in range(20):
        print('*', end='')
        if inner == 3:
            break
    print()