def dup_bit(str):
    H = 0
    x = 0
    for i in str:
        x = 1
        x<<=(ord(i)-97)

        if H&x > 0:
            print(i)
        else:
            H = x|H

    return

print(dup_bit('fearfiles'))