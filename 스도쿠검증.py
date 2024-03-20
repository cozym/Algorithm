# SW Expert Academy - 1974. 스도쿠 검증
T = int(input())

def checkOverlap(nine):
    check = True
    for i in nine:
        if nine.count(i) > 1:
            check = False
    return check

for test_case in range(1, T + 1):
    res = 1
    puzzle = []
    for i in range(9):
        puzzle.append(list(map(int,input().split())))
    for i in range(9):
        row = []
        col = []
        for j in range(9):
            row.append(puzzle[i][j])
            col.append(puzzle[j][i])
        if (not checkOverlap(row)) or (not checkOverlap(col)):
            res = 0
        position = [[0,1,2],[3,4,5],[6,7,8]]
        for k in position:
            for m in position:
                area = []
                for x in k:
                    for y in m:
                        area.append(puzzle[x][y])
                if not checkOverlap(area):
                    res = 0
    print("#{} {}" .format(test_case,res))
