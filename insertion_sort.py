def operate(lis,i):
    j=i
    while j>0:
        if lis[j]<lis[j-1]:
            lis[j],lis[j-1]=lis[j-1],lis[j]
        j-=1
    return lis

def insertion_sort(lis):
    for i in range(0,len(lis)-1):
        if lis[i]>lis[i+1]:
            lis = operate(lis,i+1)
    return lis

print(insertion_sort([2,4,5,1,8,3,6]))