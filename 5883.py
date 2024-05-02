# 아이폰 9S
import sys
input = sys.stdin.readline

N = int(input())
capacity = []
for _ in range(N):
    capacity.append(int(input()))
kinds = set(capacity)
res = 0

for target in kinds:
    sequence = 0
    pre = -1
    for i in capacity:
        if i==target:
            continue
        if i != pre:
            pre = i
            sequence = 1
        else:
            sequence += 1
        res = max(sequence, res)

print(res)