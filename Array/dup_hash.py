def dup_hash(lis):
    m = max(lis)+1
    has = [0]*m
    for i in lis:
        has[i]+=1

    for i in range(1,len(has)):
        if has[i]>1:
            print(i,'-',has[i])
    return


print(dup_hash([2,4,3,3,3,7,6,8,8,9,6,6]))