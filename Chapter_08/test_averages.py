# This program reads test scores from a CSV file
# and calculates each student's test average.

def main():
    # Read the CSV file's lines into a list.
    with open('test_scores.csv', 'r') as csv_file:
        lines = csv_file.readlines()

    # Process the lines.
    for line in lines:
        # Get the test scores as tokens.
        tokens = line.split(',')
        
        # Calculate the total of the test scores.
        total = 0.0
        for score in tokens:
            total += float(score)
        
        # Calculate the average of the test scores.
        average = total / len(tokens)
        print(f'Average: {average}')

# Execute the main function.
if __name__ == '__main__':
    main()