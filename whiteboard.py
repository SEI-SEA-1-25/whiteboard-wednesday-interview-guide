def sum(num):
    sums = 0
    count = 0
    for i in num:
        if i < 0:
            sums += i
        else:
            count += 1
    return [count, sums]


 