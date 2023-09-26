def aVeryBigSum(ar):
    longSum = 0
    n = len(ar)
    for i in range(0, n):
        longSum += ar[i]
    return longSum


ar = [10000001, 10000002, 10000003, 10000004, 10000005]
Ans = aVeryBigSum(ar)
print(Ans)
