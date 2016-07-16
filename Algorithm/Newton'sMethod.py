
def evaluate_poly(poly,x):
    result = 0.0

    for i in xrange(len(poly)):
        coe = poly[i]
        result += coe*(x**i)
          
    ##print result
    return result
        
        
        
def derivatives(poly):

    result=[]

    
    for i in xrange(1, len(poly)):
     
        result.append(float(i*poly[i]))
    ##print result
    return result
        





def compute_root(poly,x_0,epsilon):
    ##print (poly)
    root = x_0
    counter = 1
    while abs(evaluate_poly(poly,root)) >= epsilon:
        root = (root - evaluate_poly(poly,root)/evaluate_poly(derivatives(poly),root))
        ##print x_0
        counter += 1  
    
    return [root, counter]
    


polynomial = (-13.39, 0.0, 17.5, 3.0, 1.0)
x_0 = 0.1
epsilon = .0001
print (compute_root(polynomial,x_0,epsilon))

        
