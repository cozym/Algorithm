# 일곱 난쟁이
import sys

heights = []
for i in range(9):
    heights.append(int(sys.stdin.readline()))
res = heights[:]
twosum = sum(heights)-100

# 다 더하고 2개씩 묶어서 빼봤을 때 100
for i in range(8):
    for j in range(i+1,9):
        if heights[i]+heights[j]==twosum:
            res.remove(heights[i])
            res.remove(heights[j])
            break
    if len(res)!=9:
        break

res.sort()

for p in res:
    print(p)

