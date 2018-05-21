
def f(x, y):
    a = math.floor(math.log10(y))
    return int(x*10**(1+a)+y)
