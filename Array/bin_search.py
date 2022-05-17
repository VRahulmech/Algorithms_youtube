def bin_search(lis, n):
    l = 0
    h = len(lis)
    while l<=h:
        mid = (l+h)//2
        if lis[mid]==n:
            return mid
        elif lis[mid]>n:
            h = mid-1
        else:
            l = mid+1
    return -1

print(bin_search([2,3,4,5,6],1))