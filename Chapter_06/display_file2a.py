# This program displays the contents
# of a file using the with-statement

def main():
    # Get the name of a file.
    filename = input('Enter a filename: ')

    try:
        # Open the file.
        # Using the with-statement closes the file automatically
        with open(filename, 'r') as infile:
            # Read the file's contents.
            contents = infile.read()
            # Display the file's contents.
            print(contents)

    except IOError:
        print('An error occurred trying to read')
        print('the file', filename)


# Call the main function.
if __name__ == '__main__':
    main()
