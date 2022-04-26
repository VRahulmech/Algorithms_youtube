def binary_search(lis,target):
    low = 0
    high = len(lis)-1


    while low<=high:
        mid = (low + high) // 2
        if lis[mid] == target:
            return 'the target is at '+str(mid)+'th position'
        elif lis[mid] > target:
            high = mid-1
        else:
            low = mid+1

    return 'target not found'


a = [1,2,3,4,5,11,22,33,44,55,67,78,89,90]

print(binary_search(a,5))
print(binary_search(a,12))
print(binary_search(a,6))
print(binary_search(a,44))