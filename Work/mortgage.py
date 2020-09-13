# mortgage.py
#
# Exercise 1.7 (and 1.8, 1.9)

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month_num = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    monthly_payment = payment
    if extra_payment_start_month <= month_num <= extra_payment_end_month:
        monthly_payment += extra_payment
    # print(month_num, 'payment', monthly_payment)
    principal = principal * (1+rate/12) - monthly_payment
    total_paid = total_paid + monthly_payment
    month_num += 1

print('Total paid', total_paid, 'over', month_num)