numMonths = 12
totalPaid = 0

for i in range(1,numMonths + 1):
    print 'Month: ' + str(i)
    minMonPay = round(balance * monthlyPaymentRate,2)
    balance -= minMonPay
    interest = annualInterestRate/12.0 * balance
    balance = round(balance + interest, 2)
    totalPaid += minMonPay
    print 'Minimum monthly payment: ' + str(minMonPay)
    print 'Remaining balance: ' + str(balance)
print 'Total Paid: ' + str(totalPaid)
print 'Remaining balance: ' + str(balance)
