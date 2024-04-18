# 체커
import sys
input = sys.stdin.readline

N = int(input())
checkers = []
for _ in range(N):
    x,y = map(int,input().split())
    checkers.append((x,y))
intersection = []
idx = 0

# 입력받은 체커들이 속한 x,y축들의 교점들을 검사
for x,_ in checkers:
    for _,y in checkers:
        intersection.append([])
        for cx,cy in checkers:  # 각 교점에서 체커들까지의 거리 저장
            intersection[idx].append(abs(cx-x)+abs(cy-y))
        intersection[idx].sort()    # 오름차순 정렬
        idx += 1

# k개 최솟값을 비교
for k in range(1,N+1):
    res = 1e9
    for ds in intersection:
        s = sum(ds[:k])
        if res > s:
            res = s
    print(res,end=' ')