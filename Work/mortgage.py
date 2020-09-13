# mortgage.py
#
# Exercise 1.11 (, 1.10, 1.9, 1.8 and 1.7)

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month_num = 0

extra_payment_start_month = 0
extra_payment_end_month = 0
extra_payment = 0

while principal > 0:
    monthly_payment = payment
    if extra_payment_start_month <= month_num <= extra_payment_end_month:
        monthly_payment += extra_payment
    # print(month_num, 'payment', monthly_payment)
    principal = principal * (1+rate/12) - monthly_payment
    total_paid = total_paid + monthly_payment
    month_num += 1
    if principal < 0:
        principal = 0.00
    print(month_num, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Months', month_num)