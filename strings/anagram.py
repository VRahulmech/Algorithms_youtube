def ana(str1, str2):
    H=[0]*26
    for i in range(len(str1)):
        H[ord(str1[i])-97]+=1

    for j in range(len(str2)):
        H[ord(str2[j])-97]-=1

    if H == [0]*26:
        return 'Anagram'
    return 'Not Anagram'

print(ana('decimal','medical'))
print(ana('verbose','observe'))