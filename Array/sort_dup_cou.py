def sor_dup_cou(lis):
    last = -1
    for i in range(len(lis)-1):
        if lis[i]==lis[i+1] and lis[i]!=last:
            count = 1
            for j in range(i, len(lis)-1):
                if lis[j]==lis[j+1]:
                    count+=1
                else:
                    break
            last = lis[i]
            print(lis[i],'-',count)
    return

print(sor_dup_cou([2,3,3,4,5,5,5,6,8]))

