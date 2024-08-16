def sudoku(arr):
    while any(0 in arr[i] for i in range(len(arr))):

        for row in arr:
            print(row)

        print()

        full = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        prows = {index: full - set(row) for index, row in enumerate(arr)}
        cols = [[row[i] for row in arr] for i in range(len(arr[0]))]
        pcols = {index: full - set(row) for index, row in enumerate(cols)}
        boxes = {}
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = {arr[x][y] for x in range(i, i + 3) for y in range(j, j + 3)}
                boxes[(i, j)] = full - set(box)

        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == 0:
                    intersection = prows[i] & pcols[j] & boxes[(i // 3 * 3, j // 3 * 3)]
                    if len(intersection) == 1:
                        arr[i][j], = intersection

    return arr


arr = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
       [6, 0, 0, 1, 9, 5, 0, 0, 0],
       [0, 9, 8, 0, 0, 0, 0, 6, 0],
       [8, 0, 0, 0, 6, 0, 0, 0, 3],
       [4, 0, 0, 8, 0, 3, 0, 0, 1],
       [7, 0, 0, 0, 2, 0, 0, 0, 6],
       [0, 6, 0, 0, 0, 0, 2, 8, 0],
       [0, 0, 0, 4, 1, 9, 0, 0, 5],
       [0, 0, 0, 0, 8, 0, 0, 7, 9]]

for row in sudoku(arr):
    print(row)
