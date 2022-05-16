def fact_rec(n):
    if n==1:
        return 1
    return n*fact_rec(n-1)

def fact_loop(n):
    pro = 1
    for i in range(1,n+1):
        pro *= i
    return pro

print(fact_rec(5))
print(fact_loop(5))