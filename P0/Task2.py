"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

time = {}

for call in calls:
    if not time.get(call[0]):
        time.update({call[0]: int(call[3])})
    else:
        time_spent = time.get(call[0]) + int(call[3])
        time.update({call[0]: time_spent})
    
    if not time.get(call[1]):
        time.update({call[1]: int(call[3])})
    else:
        time_spent = time.get(call[1]) + int(call[3])
        time.update({call[1]: time_spent})

# print(time)

#Iterate through the dict and find the maximum 

max_key = max(time, key=time.get)

# max = 0
# for key in time:
#     if time.get(key) > max:
#         max = time.get(key)


output_string = "{} spent the longest time, {} seconds, on the phone during September 2016."

print(output_string.format(max_key, time.get(max_key)))
