#!/usr/bin/env python3

"""
7.2 Write a program that prompts for a file name, then opens that file and reads
through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
when you are testing below enter mbox-short.txt as the file name.
"""

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
scscores = []

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(':')
    score = float(line[pos+1:].strip())
    #  print(score)
    scscores.append(score)
    #  print(line)

def averagesc(list):
    tot =  0
    count = 0
    for item in list:
        tot = tot + item
        count += 1
    return tot / count

print("Average spam confidence:", averagesc(scscores))

# Result:
"""
imac2020@iMac P4E % python3 09-average-spam-confidence.py
Enter file name: mbox-short.txt
Average spam confidence: 0.7507185185185187
"""