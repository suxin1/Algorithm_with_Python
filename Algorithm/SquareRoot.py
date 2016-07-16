# square root
def Guess():
    x = int(raw_input("Enter a number:"))

    epsilon = 0.01
    step = epsilon**2
    numGuesses  = 0
    ans = 0.0

    while (abs(ans**2 -x)) >= epsilon and ans < x:
        ans += step
        numGuesses += 1


    print 'Guesses = ' + str(numGuesses)

    if (abs(ans**2 - x)) >= epsilon:
        print 'Fail to find square root of ' + str(x)
    else:
        print 'The closet answer of the square root of ' +str(x) + ' is '




# Bisection Search to find square root of a number
def BisectionSearch(x, power, epsilon):
    '''x and epsilon int or float, power an int
        epsilon > 0 & power >= 1
        returns a float y, y**power is within epsilon of x.
        if such a float dows not exist. it returns None. '''
    if x < 0 and power%2 == 0:
        return None

    numGuesses = 0

    low = min(-1, x)     # ---------------- -1 ---------- 1 ----------------------
    high = max(1, x)     # This fix the problem that this method
                         # not working with x is a fractional

    ans = (high + low)/2.0
    while abs(ans**power-x) >= epsilon:
        print 'low = ' + str(low) + 'high = ' + str(high) + 'ans = ' + str(ans)
        numGuesses += 1
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0

    print 'numGuesses = ' + str(numGuesses)

    print str(ans) + 'is close to ' + str(power) + 'th  root of ' + str(x)


BisectionSearch(8, 3, 0.001)



# Use Newton's method to find square root of a number


def Newton():
    x = int(raw_input('Enter an integer:'))

    epsilon = 0.01

    guess = x/2.0
    while abs(guess**2 -x) >= epsilon:
        guess = guess - (guess**2 - x)/(2*guess)

    print 'Sqrare root of ' + str(x) + 'is about' + str(guess)