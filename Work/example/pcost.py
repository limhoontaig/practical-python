# pcost.py
import sys


def portfolio_cost(filename):
    with open(filename,'rt') as f:
        headers = next(f)
        total_cost = 0.0
        for line in f:
            row = line.split(',')
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]

else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total Cost :', cost)
