# 보이는 점의 개수
import sys
input = sys.stdin.readline

# 1 > 3
# 홀수 > (x-1)*2
# 짝수 > (x//2)*2

# 0 > 0
# 1 > 3
# 2 > 2
# 3 > 4
# 4 > 4
# 5 > 8
# 6 > 6


res = [0]*1001
res[1] = 3
for idx in range(2,1001):
    if idx%2 == 0:
        res[idx] = res[idx-1]+idx
    else:
        res[idx] = res[idx-1]+(idx-1)*2

for _ in range(int(input())):
    print(res[int(input())])