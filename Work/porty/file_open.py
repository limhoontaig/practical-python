import csv
import sys

def portfolio_cost(filename):
    total_cost=0
    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    print(headers)
    for row in rows:
        t = (row[0], int(row[1]), float(row[2]))
        print(t)
        total_cost += t[1] * t[2]
    f.close()
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'work/data/portfolio.csv'

cost = portfolio_cost('work/data/portfolio.csv')
print('Total cost : $',cost)