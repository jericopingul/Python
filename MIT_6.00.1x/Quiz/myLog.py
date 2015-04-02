def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    power = 1
    m = b
    
    while(b < x):
        b *= m
        power += 1
        
    if(b > x):
        power -= 1
        
    return power