# report.py
#
# Exercise 2.10 (, 2.7, 2.6, 2.4)
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
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print('Warning:', row, 'Invalid row to read')
    return prices

def make_report(portfolio, prices):
    report = []
    for item in portfolio:
        name = item['name']
        report.append((name, item['shares'], prices[name], prices[name] - item['price']))
    return report

def compute_gain_loss(report):
    gain = sum([n_shares*change for name, n_shares, price, change in report])
    if gain < 0:
        print (f'Loss: {gain:.2f}')
    elif gain == 0:
        print ('No gain or loss')
    else:
        print (f'Gain: {gain:.2f}')

def display_report(report, headers):
    print(get_header_row(headers))
    print(get_header_separator(headers))
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

def get_header_row(headers):
    return ' '.join([f'{item:>10s}' for item in headers])

def get_header_separator(headers):
    return ' '.join(['-'*10 for _ in headers])


portfolio_filename = 'Data/portfolio.csv'
prices_filename = 'Data/prices.csv'
if len(sys.argv) == 3:
    portfolio_filename = sys.argv[1]
    prices_filename = sys.argv[2]

headers = ('Name', 'Shares', 'Price', 'Change')

portfolio = read_portfolio(portfolio_filename)
prices = read_prices(prices_filename)
report = make_report(portfolio, prices)
compute_gain_loss(report)
display_report(report, headers)
