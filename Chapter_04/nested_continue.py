# This program demonstrates the continue statement
# inside a nested inner loop.
for outer in range(5):
    for inner in range(20):
        if inner > 3:
            continue
        print('*', end='')
    print()