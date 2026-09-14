# This program calculates sales commissions.

# Counter variable
count = 1

# Get the number of salespeople.
salespeople = int(input('Enter the number of salespeople: '))

# Calculate each salesperson's commissions.
while count <= salespeople:
    # Get a salesperson's sales and commission rate.
    sales = float(input(f'Enter the sales for salesperson {count}: '))
    comm_rate = float(input('Enter the commission rate: '))

    # Calculate the commission.
    commission = sales * comm_rate

    # Display the commission.
    print(f'The commission is ${commission:,.2f}.')

    # Update the counter variable.
    count += 1
