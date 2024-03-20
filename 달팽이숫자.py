# SW Expert Academy .1954
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    nails = [[0 for j in range(N)] for i in range(N)]
    x,y = 0,0
    nails[y][x] = 1
    count = 2
    while count!=N*N+1:
        if x+1<N and nails[y][x+1]==0:
            x += 1
            nails[y][x] = count
            count += 1
        elif y+1<N and nails[y+1][x]==0:
            y += 1
            nails[y][x] = count
            count+=1
        elif x-1>=0 and nails[y][x-1]==0:
            x -= 1
            nails[y][x] = count
            count += 1
        else:
            while y-1 >= 0 and nails[y-1][x]==0:
                y -= 1
                nails[y][x] = count
                count += 1
    print("#{}" .format(test_case))
    for p in range(N):
        print("{}" .format(" ".join(map(str,nails[p]))))
