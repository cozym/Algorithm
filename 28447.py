# 마라탕 재료 고르기
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
ingredients = []
for _ in range(N):
    ingredients.append(list(map(int,input().split())))
res = -1e9

def recur(idx, ingre):
    if len(ingre) == K:
        global res
        flavor = 0
        for i in range(len(ingre)):
            for j in range(i+1,len(ingre)):
                flavor += ingredients[ingre[i]][ingre[j]]
        res = max(flavor,res)
        return

    if idx == N:
        return
    recur(idx+1, ingre[:])
    ingre.append(idx)
    recur(idx+1, ingre[:])

recur(0,[])
print(res)