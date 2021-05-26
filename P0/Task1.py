"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

numbers = {}

for entry in calls:
    if not numbers.get(entry[0]):
        numbers.update({entry[0]: entry[0]})
    if not numbers.get(entry[1]):
        numbers.update({entry[1]: entry[1]})

for text in texts:
    if not numbers.get(text[0]):
        numbers.update({text[0]: text[0]})
    if not numbers.get(text[1]):
        numbers.update({text[1]: text[1]})

out_string = "There are {} different telephone numbers in the records."

print(out_string.format(len(numbers)))


