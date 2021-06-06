# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
extrapayment = 1000
duration = 12
total_paid = 0.0
month = 1

while principal > 0:
    if month <= duration:
        principal = principal * (1+rate/12) - payment - extrapayment
        total_paid = total_paid + payment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

    month += 1

print('Total paid', total_paid)
print('Total month', month)
