# This program saves a list of strings to a file.

def main():
    # Create a list of strings.
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']

    # Write the list to a file.
    with open('cities.txt', 'w') as outfile:
        for item in cities:
            outfile.write(item + '\n')

# Call the main function.
if __name__ == '__main__':
    main()