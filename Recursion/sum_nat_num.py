def sum_nat_rec(n):
    if n==1:
        return 1
    elif n>1:
        return n+sum_nat_rec(n-1)

def sum_nat_formula(n):
    return n*(n+1)/2

def sum_nat_loop(n):
    sum = 0
    for i in range(n+1):
        sum+=i
    return sum

print(sum_nat_rec(5))
print(sum_nat_formula(5))
print(sum_nat_loop(5))