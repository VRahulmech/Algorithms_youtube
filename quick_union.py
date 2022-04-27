n = int(input('enter number of objects: '))
id = list(range(n))

while True:
    def root(i):
        while i != id[i]:
            i = id[i]
        return i

    def connected(p,q):
        if root(p)==root(q):
            print('True')
        else:
            print('False')
        return

    def union(p,q):
        pid = root(p)
        qid = root(q)
        id[pid]=qid
        return


    inp = input()

    if inp == 'union':
        union(int(input('first: ')), int(input('second: ')))
    elif inp == 'connected':
        connected(int(input('first: ')), int(input('second: ')))
    else:
        break
