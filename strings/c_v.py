def con_vowel(str):
    v_count = 0
    count = 0
    for i in str:
        if i in ['a','A','e','E','i','I','o','O','u','U']:
            v_count+=1
        elif ord(i)>=65 or ord(i)<=90 or ord(i)>=97 or ord(i)<=122:
            count +=1
    print('vowels are ',v_count,'in number')
    print('consonents are ', count, 'in number')
    return


print(con_vowel('I am Vasala Rahul'))