# This program reads numbers from a file into a list.

def main():
    # Read the contents of the file into a list.
    with open('numberlist.txt', 'r') as infile:
        numbers = infile.readlines()

    # Convert each element to an int.
    for index in range(len(numbers)):
        numbers[index] = int(numbers[index])

    # Print the contents of the list.
    print(numbers)

# Call the main function.
if __name__ == '__main__':
    main()