# report.py
#
# Exercise 2.7 (, 2.6, 2.4)
import sys
import csv

def read_portfolio(filename):
    """
    Read from portfolio file and return the list of portfolio holdings

    :param filename: Portfolio file
    :returns list of portfolio holdings
    """
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name': row[0],
            'shares': int(row[1]),
            'price': float(row[2])}
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    """
    Read from prices file and return the list of stock prices

    :param filename: Prices file
    :returns list of stock prices
    """
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print('Warning:', row, 'Invalid row to read')
    return prices

portfolio_filename = 'Data/portfolio.csv'
prices_filename = 'Data/prices.csv'
if len(sys.argv) == 3:
    portfolio_filename = sys.argv[1]
    prices_filename = sys.argv[2]

portfolio = read_portfolio(portfolio_filename)
prices = read_prices(prices_filename)

total_purchase_price = 0.0
total_current_price = 0.0
for item in portfolio:
    name = item['name']
    n_shares = item['shares']
    purchase_price = n_shares * item['price']
    current_price = purchase_price
    if name in prices:
        current_price = n_shares * prices[name]
    total_purchase_price += purchase_price
    total_current_price += current_price

print('Total purchase price', total_purchase_price)
print('Total current price', total_current_price)
print('Status:', 'Gain' if total_purchase_price < total_current_price else 'Loss')