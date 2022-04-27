n = int(input('enter number of objects: '))
id = list(range(n))
print(id)

while True:
    def union(p,q):
        pid = id[p]
        qid = id[q]
        for i in range(p,q):
            if id[i]==pid:
                id[i]=qid
        print(id)
        return

    def connected(p,q):
        print(id[p]==id[q])
        return

    inp = input()

    if inp=='union':
        union(int(input('first: ')),int(input('second: ')))
    elif inp=='connected':
        connected(int(input('first: ')),int(input('second: ')))
    else:
        break