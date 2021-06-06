# pcost.py


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

cost = portfolio_cost('data/portfolio.csv')
print('Total Cost :', cost)

