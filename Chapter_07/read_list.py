# This program reads a file's contents into a list.

def main():
    # Read the contents of the file into a list.
    with open('cities.txt', 'r') as infile:
        cities = infile.readlines()
    
    # Strip the \n from each element.
    for index in range(len(cities)):
        cities[index] = cities[index].rstrip('\n')

    # Print the contents of the list.
    print(cities)

# Call the main function.
if __name__ == '__main__':
    main()