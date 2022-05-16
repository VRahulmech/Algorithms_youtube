def funA(n):
    while n>0:
        print(n)
        funB(n-1)
        return

def funB(n):
    while n>1:
        print(n)
        funA(n//2)
        return


funA(20)
