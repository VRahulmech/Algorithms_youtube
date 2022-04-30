
def push(self,n):
    self.append(n)
    return

def pop(self):
    self.pop()
    return


if __name__ == '__main__':
    st = []
    push(st,17)
    push(st,3)
    print(st[::-1])
    pop(st)
    push(st,34)
    print(st[::-1])
    pop(st)
    push(st,21)
    print(st[::-1])