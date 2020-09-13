# report.py
#
# Exercise 2.4
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
                print(row, 'Invalid row to read')
    return prices
