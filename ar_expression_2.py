from algs4.stack import Stack

def ar_exp(sti):
    opr = Stack()
    num = Stack()

    for i in range(len(sti)):
        st=sti[i]
        if st in ['+','*']:
            opr.push(st)
        elif st == ')':
            op = opr.pop()
            if op == '+':
                num.push(num.pop()+num.pop())
            elif op == '*':
                num.push(num.pop()*num.pop())
        elif st == '(':
            pass
        elif st == ' ':
            break
        else:
            num.push(float(st))

    print(num.pop())
    return

ar_exp('(1+((2+3)*(4*5)))')