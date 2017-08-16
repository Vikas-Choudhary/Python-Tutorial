#creates the fibonaaci sequence in LogN time complexity
def fibonacci(n):
    a = 1
    b = 1
    c = 1
    rc = 0
    tc=0
    d = 0
    rd = 1
 
    while (n > 0):
    
        #print(n)
        if n % 2 == 1:
            tc = rc
            rc = rc*a + rd*c
            rd = tc*b + rd*d
        ta = a
        tb = b
        tc = c
        a = a*a  + b*c
        b = ta*b + b*d
        c = c*ta + d*c
        d = tc*tb+ d*d

        n = (int)(n / 2)
    
    return rc;
for i in range(0,100+1):
    print(i, "  ",fibonacci(i))
