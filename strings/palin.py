def palin(str):
    lis= list(str.lower())
    if str == ''.join(reversed(lis)):
        return 'palindrome'
    else:
        return 'not palindrome'

print(palin('NItin'))