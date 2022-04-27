n = int(input('enter number of objects: '))
id = list(range(n))
sz = dict()
for i in range(n):
    sz[i]=1
sz1 = sz

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
        global sz
        pid = root(p)
        qid = root(q)
        if pid==qid:
            return
        else:
            print(pid, qid)
            if sz.get(p, 1) <= sz.get(q, 1):
                #print(sz)
                id[pid] = qid
                sz1[qid] += sz[pid]
            else:
                id[qid] = pid
                sz1[pid] += sz[qid]
        sz = sz1

    inp = input()

    if inp == 'union':
        union(int(input('first: ')), int(input('second: ')))
    elif inp == 'connected':
        connected(int(input('first: ')), int(input('second: ')))
    else:
        break