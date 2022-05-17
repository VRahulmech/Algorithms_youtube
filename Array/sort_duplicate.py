def sort_dup(lis):
    last = -1
    for i in range(len(lis)-1):
        if lis[i]==lis[i+1]:
            if last!= lis[i]:
                last = lis[i]
                print(lis[i])
    return

print(sort_dup([2,3,3,3,4,6,7,8,9,9]))
            