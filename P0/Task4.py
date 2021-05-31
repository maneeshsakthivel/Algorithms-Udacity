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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

"""
Traverse calls and find out only numbers wihch call and have no incoming calls
"""
final_liust = []
for call in calls:
    if call[0] not in final_liust:
        final_liust.append(call[0])

for call in calls:
    if call[1] in final_liust:
        final_liust.remove(call[1])


for text in texts:
    if text[0] in final_liust:
        final_liust.remove(text[0])

    if text[1] in final_liust:
        final_liust.remove(text[1])

final_liust.sort()
print("These numbers could be telemarketers: ")
# print(len(final_liust))
for number in final_liust:
    print(number)


