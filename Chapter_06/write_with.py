# This program wites the numbers 0-9 to sequence.txt.
def main():
    with open('sequence.txt', 'w') as outfile:
        for number in range(10):
            outfile.write(f'{number}\n')
    print('Data written to sequence.txt.')

# Call the main function.
if __name__ == '__main__':
    main()
