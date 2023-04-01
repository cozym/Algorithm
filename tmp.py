import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N,L,R = map(int, input().split())
population = []
population = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1,0,1,0],[0,-1,0,1]

def dfs(x,y):
    global check
    global union_list
    for i in range(4):
        nx= x+dx[i]
        ny = y+dy[i]
        
        if 0 <= nx <N and 0 <= ny <N and check[nx][ny]:
            if L <= abs(population[x][y]-population[nx][ny]) <= R:
                check[nx][ny] = True
                union_list.append([nx,ny])
                dfs(nx,ny)

while(1):
    check = [ False * N for _ in range(N)]
    for i in range(population):
        for j in range(population[i]):
            union_list = []
            if check[i][j]:
                union_list.append([i,j])
                check[i][j] = True
                dfs(i,j)

                if len(union_list) > 1:
                    