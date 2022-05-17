def unsort_dup(lis):
    for i in range(len(lis)-1):
        if lis[i]==-1:
            continue
        count = 1
        for j in range(i+1,len(lis)):
            if lis[i]==lis[j]:
                count+=1
                #print(lis)
                lis[j]=-1
                #print(lis)

        if count>1:
            print(lis[i],'-',count)
    return

print(unsort_dup([2,4,3,3,3,7,6,8,8,9,6,6]))