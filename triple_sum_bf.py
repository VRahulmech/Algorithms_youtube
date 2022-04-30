def triple_sum(lis):
    triple = []
    count = 0
    for i in lis:
        for j in lis:
            if (i != j):
                for k in lis:
                    if (k!=i) and (j!=k):
                        if (i+j+k == 0) and (set([i,j,k]) not in triple):
                            triple.append(set([i,j,k]))
                            count+=1
    return triple,count

print(triple_sum([30,-40,-20,-10,40,0,10,5]))