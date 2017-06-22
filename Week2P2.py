balance = 320000
annualInterestRate = 0.2

balanceEnd = balance
paymentLower = balance/12
paymentUpper = balance*(1+annualInterestRate)/12

while True:
    payment = ( paymentLower + paymentUpper ) / 2

    for months in range(0,12):
        balanceEnd = (balanceEnd - payment) * (1 + annualInterestRate / 12)

    if balanceEnd <= 0 and (paymentUpper - paymentLower) <= 0.01:
        break
    elif balanceEnd > 0:
        paymentLower = payment
        balanceEnd = balance
    else:
        paymentUpper = payment
        balanceEnd = balance


print("Lowest payment:", round(payment, 2))

