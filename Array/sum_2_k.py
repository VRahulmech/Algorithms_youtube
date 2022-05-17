def sum_k(lis,n):
    for i in range(len(lis)-1):
        for j in range(i+1,len(lis)-1):
            if lis[i]+lis[j]==n:
                print(lis[i],'+',lis[j],'=',n)
    return

print(sum_k([6,3,8,10,16,7,5,2,9,14],10))