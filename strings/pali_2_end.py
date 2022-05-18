def pali_2_end(str):
    count = 0
    for i in range(len(str)//2+1):
        if str[i].lower() == str[len(str)-i-1].lower():
            count+=1

    if count == len(str)//2+1:
        return 'palindrome'
    return 'not palindrome'

print(pali_2_end('zoyoz'))