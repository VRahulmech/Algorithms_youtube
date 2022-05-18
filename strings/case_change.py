def case_change(str):
    out = ''
    for i in str:
        if ord(i)>=65 and ord(i)<=90:
            out += chr(ord(i)+32)
        elif ord(i)>=97 and ord(i)<=122:
            out += chr(ord(i)-32)
        else:
            continue
    return out

print(case_change('RaHuL'))
