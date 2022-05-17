def lin_search(lis,n):
    for i in range(len(lis)):
        if n==lis[i]:
            if i != 0:
                lis[i], lis[0] = lis[0], lis[i]
            return i

    return -1

print(lin_search([2,3,4,5,6],5))