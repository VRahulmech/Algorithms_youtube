def max_min(lis):
    ma = mi = lis[0]
    for i in lis:
        if i<mi:
            mi=i
        elif i>ma:
            ma = i
    print('max = ',ma)
    print('min = ',mi)
    return

print(max_min([6,3,8,10,16,7,5,2,9,14]))