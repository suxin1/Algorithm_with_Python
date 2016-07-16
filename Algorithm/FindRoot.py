

def findRoot(pwr, val, epsilon):
    assert type(pwr) == int and type(val) == float and type(epsilon) == float
    low = 0.0
    high = max(val,1.0)
    ans = (high +low)/2.0
    while abs(ans**pwr - val)>= epsilon and ans <= val:
        if ans**pwr < val:
            low = ans
        else:  
            high = ans

        ans = (high + low)/ 2.0
    return ans
sqrt = findRoot(3,8.0,0.001)
print (sqrt)
  
  

##sumDigits = 0
##for c in str(1952):
##    sumDigits += int(c)
##print (sumDigits)

##x = 100
##divisors = ()
##for i in range(1,x):
##    if x%i == 0:
##        divisors = divisors+(i,)
##print (divisors)
