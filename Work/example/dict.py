# dict.py
import csv

f = open('Data/portfolio.csv')
rows = csv.reader(f)
f.close
headers = next(rows)
print(headers)
total_cost=0
for row in rows: # string data
    cost = int(row[1]) * float(row[2])
    total_cost += cost
print('Using List :', total_cost)


