def selection_sort(lis):
    for i in range(len(lis)-1):
        #print(lis,i)
        min=i
        for j in range(i+1, len(lis)):
            #print(lis,j)
            if lis[min] > lis[j]:
                min = j
                #print(min)

        if min!=i:
            lis[i],lis[min]=lis[min],lis[i]
            #print(lis)
        #print(lis,i)

    return lis

print(selection_sort([2,4,5,1,8,3,6]))