# lower and upper bounds
low = balance/12.0
up = balance*((1.0 + annualInterestRate)**12)/12.0
monthlyRate = annualInterestRate/12.0

numMonths = 1
totalCost = 0
origBal = balance

epsilon = 0.01 #tolerance
interest = 0
lowPay = (up + low)/2.0


while(abs(balance) >= epsilon and numMonths <= 12):
    balance -= lowPay
    balance += interest
    interest = balance*monthlyRate
    
    # paying too little
    if(balance > epsilon and numMonths == 12):
        balance = origBal
        numMonths = 0
        low = lowPay
        lowPay = (up + low)/2.0

    # paying too much
    elif(balance < -epsilon and numMonths == 12):
        balance = origBal
        numMonths = 0
        up = lowPay
        lowPay = (up + low)/2.0    

    numMonths += 1


print 'Lowest Payment: ' + str(round(lowPay,2))
