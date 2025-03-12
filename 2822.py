# 점수 계산
import sys
input = sys.stdin.readline

scores = []
for i in range(1,9):
    s = int(input())
    scores.append([s,i])

scores.sort(reverse=True)
total = 0
nums = []
for i in range(5):
    score, idx = scores[i]
    total += score
    nums.append(idx)

nums.sort()

print(total)
print(*nums)