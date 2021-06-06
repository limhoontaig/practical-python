# dict.py
import csv

f = open('Data/portfolio.csv')
rows = csv.reader(f)
f.close
headers = next(rows)
total_cost=0
total_cost = sum([int(row[1]) * float(row[2]) for row in rows])
print('Using List Comprehension:', total_cost)
