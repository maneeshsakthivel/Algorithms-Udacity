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

# print(calls)

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

first_string = "First record of texts, {} texts {} at time {}"
 
print (first_string.format(texts[0][0], texts[0][1], texts[0][2]))

second_string = "Last record of calls, {} calls {} at time {}, lasting {} seconds"
# print(calls[-1])
print (second_string.format(calls[-1][0], calls[-1][1], calls[-1][2], calls[-1][3]))

 
"""
Time complexity:
Since accesing using index would be O(1) and the elements are being accesed via their indexes the overall complexity would be O(1)

Overall Complexity - O(1)
"""

