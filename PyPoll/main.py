# imports
import os
import csv

# make sure this is the file being run
if (__name__ == "__main__"):
    # change working directory to file directory
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # set file locations and names
    input_file = os.path.join("Resources", "election_data.csv")
    output_file = os.path.join("analysis", "election_results.txt")

    # variables
    total_votes = 0
    candidates = {}

    # open input files
    with open(input_file, "r") as input_csv:
        # use csv reader
        csvreader = csv.reader(input_csv, delimiter=",")

        # skip header
        csv_header = next(csvreader)

        # loop through input file and iterate votes for each candidate
        for row in csvreader:
            candidate = row[2]

            if candidate in candidates:
                candidates[candidate] += 1
            else:
                candidates[candidate] = 1

            total_votes += 1

    # find the winner
    winner = list(candidates.keys())[
        list(candidates.values()).index(max(candidates.values()))
        ]

    # start list for output strings
    output_strings = [
        "Election Results",
        "-------------------------",
        f"Total Votes: {total_votes}",
        "-------------------------",
    ]

    # add each candidate, their percentage of votes, and number of votes
    # to output strings
    for name, votes in candidates.items():
        output_strings.append(f"{name}: {votes / total_votes * 100:.3f}% "
                              f"({votes})")

    # add final lines to output strings
    output_strings.append("-------------------------")
    output_strings.append(f"Winner: {winner}")
    output_strings.append("-------------------------")

    for string in output_strings:
        print(string)

    with open(output_file, "w") as output_txt:
        for line in output_strings:
            output_txt.write(line + "\n")
