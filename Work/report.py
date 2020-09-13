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
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio
