def rec_binary_search(lis, target):
    if len(lis)==0:
        return 'target not found'
    else:
        low = 0
        high = len(lis)-1
        mid = (low+high)//2

        if lis[mid]==target:
            return 'the target is present'
        elif lis[mid]>target:
            return rec_binary_search(lis[:mid-1],target)
        else:
            return rec_binary_search(lis[mid+1:],target)
        return 'target not found'

a = [1,2,3,4,5,11,22,33,44,55,67,78,89,90]

print(rec_binary_search(a,5))
print(rec_binary_search(a,12))
print(rec_binary_search(a,6))
print(rec_binary_search(a,44))