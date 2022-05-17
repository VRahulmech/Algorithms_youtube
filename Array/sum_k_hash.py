def sum_k_hash(lis,n):
    has = [0]*(max(lis)+1)
    for i in lis:
        if has[n-i]>=1:
            print(i,'+',n-i,'=',n)
        has[i]+=1
    return

print(sum_k_hash([6,3,8,10,16,7,5,2,9,14],10))