def check_Power(N,k):
    if N <= 0 or k <=0:
        print "not a valid input"
    else:
        for i in range (1,20):
            x = k**i
            if x == N :
                print " True "
                print k, "power ", i , "is", N
                break
            elif x> N:
                print "false"
                break
check_Power(4096, 16)
check_Power(0, 98)
check_Power(9,3)
