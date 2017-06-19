balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Paste your code into this box
for month in range(12):
    balance -= monthlyPaymentRate * balance
    balance += annualInterestRate / 12 * balance

print("Remaining balance: %.2f" % balance)
