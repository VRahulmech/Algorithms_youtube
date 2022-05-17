def bin_sea_rec(lis,l,h, n):
    mid = (l+h)//2
    if l<=h:
        if lis[mid]==n:
            return mid
        elif lis[mid]>n:
            return bin_sea_rec(lis,l,mid-1,n)
        else:
            return bin_sea_rec(lis,mid+1,h,n)
    return -1

print(bin_sea_rec([2,3,4,5,6],0,len([2,3,4,5,6]),6))