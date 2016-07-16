#int to binary
def intTobin():
    num = int(raw_input('Enter a number:'))
    if num < 0:
        isNeg = True
        num = abs(num)
    else:
        isNeg = False
    result = ''

    if num == 0:
        result = '0'


    while num > 0:
        result = str(num%2) + result
        num = num/2


    if isNeg:
        result = '-' + result
    print result



# Decimal to binary
def decTobin():
    x = float(raw_input('Enter a decimal number between 0 and 1:'))

    p = 0
    while ((2**p)*x)%1 != 0:
        print ('Remainder = ' + str((2**p)*x - int((2**p)*x)))
        p += 1
    # if there is no integer p such that x*(2**p) is a integer,
    # the internal representation is always an approximation
    # When we compare two float number it's better to do like this abs(x-y) < 0.00001

    num = int(x*(2**p))

    result = ''
    if num == 0:
        result = '0'
    while num > 0:
        result = str(num%2) + result
        num = num/2

    for i in range(p - len(result)):
        result = '0' + result

    result = result[0:-p] + '.' + result[-p:]
    print 'The binary representation of the decimal ' + str(x) + ' is ' + str(result)