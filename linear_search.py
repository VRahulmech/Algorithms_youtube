def linear_search(list, target):
    for i in range(0,len(list)):
        if list[i] == target:
            return 'the target is in '+str(i)+' position'
    return 'target not found'

a = [0,1,23,5,6,7,9,3,10]

print(linear_search(a,3))
print(linear_search(a,23))
print(linear_search(a,4))