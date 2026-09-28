# This program reads test scores from a CSV file and calculates each student's test average.
# Uses the csv module
import csv

def main():
    # Open the CSV file.
    with open('test_scores.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        # Process each row.
        for row in reader:
            # Calculate the total of the test scores.
            total = 0.0
            for score in row:
                total += float(score)

            # Calculate the average of the test scores.
            average = total / len(row)
            print(f'Average: {average}')

# Execute the main function.
if __name__ == '__main__':
    main()