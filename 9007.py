# 카누 선수
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k,n = map(int,input().split())
    students = []
    combi12 = []
    combi34 = []
    for i in range(4):
        students.append(list(map(int,input().split())))
    for a in range(n):
        for b in range(n):
            combi12.append(students[0][a] + students[1][b])
            combi34.append(students[2][a] + students[3][b])
    combi12.sort()
    combi34.sort()
    L = len(combi34)
    l,r = 0,L-1
    res = 0
    distance = int(1e9)
    while l < L and 0 <= r:
        s = combi12[l]+combi34[r]
        if abs(k-s) < distance:
            distance = abs(k-s)
            res = s
        elif abs(k-s) == distance:
            res = min(res, s)
        if s >= k:
            r -= 1
        else:
            l += 1
    print(res)