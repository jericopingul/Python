numMonths = 1
totalCost = 0
origBal = balance

epsilon = 10 # step size
lowPay = epsilon
interest = 0

while(True):
    balance -= lowPay
    balance += interest
    interest = balance*annualInterestRate/12.0
    if(balance > 0 and numMonths == 12):
        balance = origBal
        numMonths = 0
        lowPay += epsilon
    elif(balance < 0 and numMonths == 12):
        break
    numMonths += 1


print 'Lowest Payment: ' + str(lowPay)
