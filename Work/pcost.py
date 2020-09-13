# pcost.py
#
# Exercise 1.33 (, 1.32, 1.31, 1.30, 1.27)

import sys
import csv

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                name, n_shares, cost = row
                total_cost += int(n_shares) * float(cost)
            except ValueError:
                print('Error occured.')
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
total_cost = portfolio_cost(filename)
print('Total cost', total_cost)