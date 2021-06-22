import csv
import sys

def portfolio_cost(filename):
    total_cost=0
    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    print(headers)
    names = []
    portfolio = []
    for row in rows:
        d = {
            'name' : row[0],
            'shares' : int(row[1]),
            'price' : float(row[2])
        }
        items = d.items()
        total_cost += d['shares'] * d['price']
        portfolio.append(items)

        names.append(row[0])
    f.close()
    return total_cost, portfolio, names

def unique(names):
    unique = set(names)
    return unique


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'work/data/portfolio.csv'

cost_names = portfolio_cost('work/data/portfolio.csv')
print('Total cost : $',cost_names[0])
print(cost_names[1])
unique_names = unique(cost_names[2])
print(cost_names[1])
print(unique_names)