def sin_mis_any(lis):
    low = lis[0]
    diff = low-0
    for i in range(len(lis)):
        if lis[i]-i!=diff:
            return i+diff
    return -1

print(sin_mis_any([4,5,6,8,9,10]))