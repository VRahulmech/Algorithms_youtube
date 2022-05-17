def sort_sum_k(lis,n):
    i = 0
    j = len(lis)-1
    while i<=j:
        if lis[i]+lis[j]==n:
            print(lis[i],'+',lis[j],'=',n)
            i+=1
            j-=1
        elif lis[i]+lis[j]<n:
            i+=1
        else:
            j-=1
    return

print(sort_sum_k([2,3,4,5,6,7,8,9,11,13],10))