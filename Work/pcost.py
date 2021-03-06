# pcost.py
#
# Exercise 2.15 (, 1.33, 1.32, 1.31, 1.30, 1.27)

import sys
import csv

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows, 1):
            holding = dict(zip(headers, row))
            try:
                n_shares = int(holding['shares'])
                cost = float(holding['price'])
                total_cost += n_shares * cost
            except ValueError:
                print('Row',i,': Couldn\'t convert: ', row)
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
total_cost = portfolio_cost(filename)
print('Total cost', total_cost)