# pcost.py
#
# Exercise 1.27

total_cost = 0.0
with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        name, n_shares, cost = line.split(',')
        total_cost += int(n_shares) * float(cost)
print('Total cost', total_cost)