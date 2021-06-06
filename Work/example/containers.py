# containers.py

import csv

records = [] # initial empty list

with open('data/portfolio.csv','rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        records.append((row[0], int(row[1]), float(row[2])))
print(records)


# prices = {} # Initial empty dict

# with open('Data/prices.csv', 'rt') as f:
#     headers = next(f)
#     for line in f:
#         row = line.split(',')
#         prices[row[0]] = float(row[1])
# print(prices)