# This program displays the total of the
# amounts in the sales_data.txt file.

def main():
    # Initialize an accumulator.
    total = 0.0
    
    try:
        # Open the sales_data.txt file.
        with open('sales_data.txt', 'r') as infile:
            # Read the values from the file and accumulate them.
            for line in infile:
                amount = float(line)
                total += amount

    except Exception as err:
        print(err)
    else:
        # Print the total.
        print(f'{total:,.2f}')

# Call the main function.
if __name__ == '__main__':
    main()