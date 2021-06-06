# dict.py
import csv

f = open('Data/portfolio.csv')
rows = csv.reader(f)
f.close
headers = next(rows)
total_cost=0
for row in rows:
    t = (row[0],int(row[1]),float(row[2]))
    cost = t[1]*t[2]
    total_cost += cost
print('Tuple method:', f'{total_cost:0.2f}')
