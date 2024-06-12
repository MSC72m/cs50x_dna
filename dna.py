import csv
import sys


def main():
    # Check if correct number of command-line arguments provided
    if len(sys.argv) != 3:
        print("Please provide valid input: python script.py <csv_file_path> <dna_sequence_file_path>")
        sys.exit(1)

    # Read DNA data from CSV file
    database = []
    with open(sys.argv[1]) as csv_file:
        database = list(csv.DictReader(csv_file))

    # Read DNA sequence from file
    with open(sys.argv[2]) as sequence_file:
        sequence = sequence_file.read()

    # Get the list of STRs from the first row of the database
    strs = list(database[0].keys())
    strs.remove('name')  # Remove 'name' column

    # Calculate the longest match for each STR in the DNA sequence
    profile = {}
    for STR in strs:
        match_length = longest_match(sequence, STR)
        profile[STR] = match_length

    # Find the person with the closest match to the DNA sequence
    match_name = find(database, profile)
    print(match_name)


def find(database, profile):
    """Find the person with the closest match to the DNA profile."""
    for person in database:
        if all(int(profile[STR]) == int(person[STR]) for STR in profile):
            return person['name']
    return "No match"


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):

        count = 0

        while True:

            start = i + count * subsequence_length
            end = start + subsequence_length

            if sequence[start:end] == subsequence:
                count += 1

            else:
                break

        longest_run = max(longest_run, count)

    return longest_run


main()
