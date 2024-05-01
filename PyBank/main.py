import os
import csv


if (__name__ == "__main__"):
    # Change working directory to the directory of the script file
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # set file names and locations
    input_file = os.path.join("Resources", "budget_data.csv")
    output_file = os.path.join("analysis", "analysis.txt")

    # initialize variables
    net_profit = 0
    dates = []
    profit_changes = []
    total_months = 0
    previous_profit = 0
    total_change = 0

    # open input file and read data
    with open(input_file, 'r') as budget_csv:
        # use csv reader
        csvreader = csv.reader(budget_csv, delimiter=",")

        # read in header row
        header_row = next(csvreader)

        # read data from each row and store it
        for row in csvreader:
            # set working variables
            month = row[0]
            current_profit = int(row[1])

            # add changes
            total_months += 1
            net_profit += current_profit
            current_profit_change = current_profit - previous_profit

            # store data
            profit_changes.append(current_profit_change)
            dates.append(month)

            # set up for next row
            previous_profit = current_profit

    # remove first index because there is no change
    profit_changes.pop(0)

    # calculate average change
    for change in profit_changes:
        total_change += change
    average_change = total_change / len(profit_changes)

    # find and store max values and dates
    greatest_increase = max(profit_changes)
    greatest_decrease = min(profit_changes)
    greatest_increase_month = dates[profit_changes.index(greatest_increase)]
    greatest_decrease_month = dates[profit_changes.index(greatest_decrease)]

    # store output strings with correct values
    output_strings = [
        "Financial Analysis",
        "----------------------------",
        f"Total Months: {total_months}",
        f"Total: ${net_profit}",
        f"Average Change: ${average_change:.2f}",
        f"Greatest Increase in Profits: {greatest_increase_month} "
        f"(${greatest_increase})",
        f"Greatest Decrease in Profits: {greatest_decrease_month} "
        f"(${greatest_decrease})"
    ]

    # output strings in terminal and in a file
    with open(output_file, 'w') as output:
        for string in output_strings:
            print(string)
            output.write(string + "\n")
