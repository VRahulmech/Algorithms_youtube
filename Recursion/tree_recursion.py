def func(n):
    while n>0:
        print(n)
        func(n-1)
        func(n-1)
        return
    
func(3)