# DNA

## Project Description
This project is a DNA matching program that reads a CSV file containing DNA profiles and a text file containing a DNA sequence. It calculates the longest match of specific Short Tandem Repeats (STRs) in the DNA sequence and compares it against the profiles in the database to identify the individual.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm Explanation](#algorithm-explanation)
- [Code Explanation](#code-explanation)

## Installation
No special installation is required for this project. Ensure you have Python installed.

## Usage
To run the project, use the following command:
``` python
python script.py <csv_file_path> <dna_sequence_file_path>
```
You need to provide the path to the CSV file containing DNA profiles and the path to the text file containing the DNA sequence.

## Algorithm Explanation
The algorithm works as follows:

### Read the Input Files:
The program reads the DNA profiles from a CSV file.
It reads the DNA sequence from a text file.
### Calculate Longest STR Matches:
The program calculates the longest match for each STR in the DNA sequence.
### Find Matching Profile:
It compares the STR matches against the profiles in the database.
It identifies the individual with the closest match to the DNA sequence.
## Code Explanation
Importing Libraries
``` python

import csv
import sys
These import the csv and sys libraries to handle CSV file reading and command-line arguments, respectively.

Main Function
python
Copy code
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
```
Checks if the correct number of command-line arguments are provided.
Reads the DNA profiles from the specified CSV file.
Reads the DNA sequence from the specified text file.
Extracts the list of STRs from the first row of the database.
Calculates the longest match for each STR in the DNA sequence.
Finds and prints the name of the person with the closest match to the DNA sequence.
Find Function
```python

def find(database, profile):
    """Find the person with the closest match to the DNA profile."""
    for person in database:
        if all(int(profile[STR]) == int(person[STR]) for STR in profile):
            return person['name']
    return "No match"
```
Iterates through each person in the database.
Compares each STR count in the profile to find the person with the closest match.
Returns the name of the matching person or "No match" if no match is found.
Longest Match Function
```python

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
```
Initializes variables to track the longest run of a subsequence.
Iterates through the sequence to find the longest consecutive run of the subsequence.
Updates and returns the longest run found.
Running the Main Function
```python

main()
```
Calls the main function to execute the program.
