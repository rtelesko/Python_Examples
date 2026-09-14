# This program reads the contents of sequence.txt.
def main():
    with open('sequence.txt', 'r') as infile:
        line = infile.read()
        while line != '':
            print(f'{line}')
            line = infile.read()

# Call the main function.
if __name__ == '__main__':
    main()
