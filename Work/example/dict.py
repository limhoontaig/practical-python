# dict.py
import csv

f = open('Data/portfolio.csv')
rows = csv.reader(f)
f.close
headers = next(rows)
total_cost=0
for row in rows:
    d = {
        'name':row[0],
        'shares':int(row[1]),
        'price':float(row[2])
    }
    cost = d['shares']*d['price']
    total_cost += cost
print('Dictionary method:', f'{total_cost:0.2f}')
