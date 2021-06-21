import csv
import sys

def portfolio_cost(filename):
    total_cost=0
    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    print(headers)
    for row in rows:
        d = {
            'name' : row[0],
            'shares' : int(row[1]),
            'price' : float(row[2])
        }
        print(d)
        total_cost += d['shares'] * d['price']
    f.close()
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'work/data/portfolio.csv'

cost = portfolio_cost('work/data/portfolio.csv')
print('Total cost : $',cost)