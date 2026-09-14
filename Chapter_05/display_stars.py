# This program demonstrates default arguments.
def main():
    # Use the default arguments for cols and rows.
    display_stars()
    print()

    # Use 5 for cols and the default for rows.
    display_stars(5)
    print()

    # Use 7 for cols and 3 for rows
    display_stars(7, 3)

# This function displays rows and columns of asterisks.
def display_stars(cols=10, rows=1):
    # The outer loop prints the rows and the
    # inner loop prints the columns.
    for row in range(rows):
        for col in range(cols):
            print('*', end='')
        print()

if __name__ == '__main__':
    main()