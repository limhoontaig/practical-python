# pcost.py
import sys
import csv


def portfolio_cost(filename):
    ''' Compute the total cost (share * price) of a portfolio file '''
    total_cost = 0
    with open(filename,'rt') as f:
        headers = next(f)
        rows = csv.reader(f)
        for row in rows:
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
