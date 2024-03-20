# SW Expert Academy 1209. Sum

for test_case in range(1, 2):
    T = int(input())
    arr = []
    row = [0 for i in range(100)]
    col = [0 for i in range(100)]
    diagonal = [0,0]
    for i in range(100):
        arr.append(list(map(int,input().split())))
    
    for x in range(100):
        for y in range(100):
            if x==y:
                diagonal[0] += arr[x][y]
            if x+y == 99:
                diagonal[1] += arr[x][y]
            row[x] += arr[x][y]
            col[x] += arr[y][x]
    print("#{} {}".format(T,max(max(row),max(col),max(diagonal))))