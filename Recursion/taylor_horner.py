sum = 0
def tay_hor(m,n):
    global sum
    if n==0:
        return sum
    sum = sum*m/n + 1
    return tay_hor(m,n-1)

print(tay_hor(2,10))