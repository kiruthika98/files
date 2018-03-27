def get_all_factors(n):
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    return factors
number = int(input("Please enter the upper limit: "))
for i in range(1,number+1):
    list_of_factors = get_all_factors(i)
    if(len(list_of_factors) == 2):
        print("factors of {} are: {} and is prime!".format(i,list_of_factors))
    else:
        print("factors of {} are: {}".format(i,list_of_factors))
