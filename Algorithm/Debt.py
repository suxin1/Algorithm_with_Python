# balance = 320000
#
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04
#
# remainBalance = balance
# lowPayment = 10.0
#
# while remainBalance > 0:
#     remainBalance = balance
#     for month in range(1, 13):
#         remainingAfterPay = round(remainBalance - lowPayment, 2)
#         interests = round(remainingAfterPay * annualInterestRate/12, 2)
#
#         remainBalance = round(remainingAfterPay + interests, 2)
#     if remainBalance > 0:
#         lowPayment += 0.1
#
#
#
# print 'Lowest Payment: ' + str(lowPayment)


balance =54637546735473

annualInterestRate = 0.2

low = balance/12
high = (balance*(1+annualInterestRate/12)**12)/12

lowPayment = (low + high)/2

epsilon = 0.01

remainBalance = balance

while abs(remainBalance) > epsilon:
    remainBalance = balance
    lowPayment = round((low + high)/2, 3)
    for month in range(1, 13):
        remainingAfterPay = remainBalance - lowPayment
        interests = remainingAfterPay * annualInterestRate/12

        remainBalance = remainingAfterPay + interests

    if remainBalance > epsilon:
        low = lowPayment
    elif remainBalance < -epsilon:
        high = lowPayment


print 'Lowest Payment: ' + str(round(lowPayment,2))