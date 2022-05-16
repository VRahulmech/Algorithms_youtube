def exponent(m,n):
    if n==1:
        return m
    return m*exponent(m,n-1)

print(exponent(2,5))

def exponent_eff(m,n):
    if n==1:
        return m
    elif n==0:
        return 1
    elif n%2==0:
        return exponent_eff(m*m,n/2)
    elif n%2==1:
        return m*exponent_eff(m*m,(n-1)/2)

print(exponent_eff(2,5))