def multi_miss_hash(lis):
    ma = max(lis)
    has = [0]*(ma+1)

    for i in lis:
        has[i]+=1


    for i in range(1,len(has)):
        if has[i]==0:
            print(i)

    return

print(multi_miss_hash([2,3,6,5,1,9,8]))