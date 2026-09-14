# This program demonstrates default arguments
# and keyword arguments.
def main():
    # Display 5 rows and 10 columns.
    display_stars(rows=5, cols=10)
    print()

    # Use 7 for cols and the default for rows.
    display_stars(cols=7)
    print()

    # Use 3 for rows and the default for cols
    display_stars(rows=3)

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