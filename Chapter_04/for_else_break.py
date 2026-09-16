# This program demonstrates a loop with an else clause.
# The break statement is executed, so the else clause does not run.
for n in range(10):
    if n == 5:
        print('Breaking out of the loop.')
        break
    print(n)
else:
    print(f'After the loop, n is {n}.')
