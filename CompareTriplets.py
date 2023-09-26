def compareTriplets(a, b):
    alicePoint = 0
    bobPoint = 0
    n = len(a)
    for i in range(0, n):
        if a[i] == b[i]:
            continue

        elif a[i] < b[i]:
            print("Bob gets 1 point")
            bobPoint += 1
        elif a[i] > b[i]:
            alicePoint += 1
            print("Alice gets 1 point")
    ans = [alicePoint, bobPoint]
    return ans


a = [5, 6, 7]
b = [3, 6, 10]
result = compareTriplets(a, b)
print(result)
