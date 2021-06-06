
# f = open('Data/portfolio.dat','rt')
# data = f.read()
# print(data)
# f.close()

import csv
filename = 'Data/portfolio.csv'
f = with open (filename, 'r')
    headers = next(f)
    for line in f:
        print(line, end="")



