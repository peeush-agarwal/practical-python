# pcost.py
#
# Exercise 1.32 (, 1.31, 1.30, 1.27)

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

total_cost = portfolio_cost('Data/portfolio.csv')
print('Total cost', total_cost)