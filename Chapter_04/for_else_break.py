# This program demonstrates a loop with an else clause. In
# this example, the break statement is executed.
for n in range(10):
    if n == 5:
        print('Breaking out of the loop.')
        break
    print(n)
else:
    print(f'After the loop, n is {n}.')
