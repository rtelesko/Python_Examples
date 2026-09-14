# This program copies the sequence.txt file.
def main():
    with open('sequence.txt', 'r') as infile, open('copy.txt', 'w') as outfile:
        line = infile.read()
        while line != '':
            outfile.write(f'{line}')
            line = infile.read()
    print('The file has been copied.')

# Call the main function.
if __name__ == '__main__':
    main()
