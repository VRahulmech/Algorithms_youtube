def multi_miss(lis):
    low = lis[0]
    diff = low
    for i in range(len(lis)):
        if lis[i]-i!=diff:
            while diff<lis[i]-i:
                print(i+diff)
                diff +=1
    return

print(multi_miss([6,8,9,10,13,14,15]))
                