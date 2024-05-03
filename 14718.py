# 용감한 용사 진수
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
soldier = []
abil = [[] for _ in range(3)]
res = 1e9
for i in range(N):
    a,b,c = map(int,input().split())
    soldier.append((a,b,c))
    abil[0].append(a)
    abil[1].append(b)
    abil[2].append(c)

for idx in range(3):
    abil[idx].sort()

for s in abil[0]:
    for d in abil[1]:
        for i in abil[2]:
            cnt = 0
            for a,b,c in soldier:
                if a<=s and b<=d and c<=i:
                    cnt += 1
                if cnt == K:
                    res = min(res, s+d+i)
                    break

print(res)