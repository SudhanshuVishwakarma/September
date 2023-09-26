def simpleArraySum(ar):
    Sum = 0
    for i in range(len(ar)):
        Sum = Sum + ar[i]
    return Sum


ar = [1, 2, 3]
Ans = simpleArraySum(ar)
print(Ans)
