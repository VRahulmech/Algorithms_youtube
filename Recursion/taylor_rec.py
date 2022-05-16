p = 1
f =1
sum= 0

def eul(m,n):
    global sum,p,f
    if n==0:
        sum += 1
        return sum
    else:
        eul(m,n-1)
        p = p*m
        f = f*n
        sum += p/f
    return sum

print(eul(4,10))
