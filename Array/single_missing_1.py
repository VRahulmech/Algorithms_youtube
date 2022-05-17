def sin_mis_1(lis):
    sum_ = sum(lis)
    act_sum = lis[-1]*(lis[-1]+1)/2
    return act_sum-sum_

print(sin_mis_1([1,2,3,4,5,7,8,9]))
