# This program reads test scores from a CSV file
# and calculates each student's test average.

import csv

def main():
    try:
        with open('test_scores.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                total = 0.0

                for score in row:
                    total += float(score)

                average = total / len(row)
                print(f'Average: {average}')

    except FileNotFoundError:
        print('Error: test_scores.csv was not found.')

    except ValueError:
        print('Error: The file contains invalid test scores.')

    except ZeroDivisionError:
        print('Error: A row contains no test scores.')

# Execute the main function.
if __name__ == '__main__':
    main()