def diagonalDifference(arr):
    top_to_bottom = 0
    bottom_to_top = 0

    n = len(arr)

    col = n - 1

    for i in range(0, n):
        top_to_bottom = top_to_bottom + arr[i][i]

        bottom_to_top = bottom_to_top + arr[i][col]
        col = col - 1
    print(abs(top_to_bottom - bottom_to_top))


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = diagonalDifference(arr)
