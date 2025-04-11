# 피보나치 함수
import sys
input = sys.stdin.readline

fibo = [[1,0],[0,1]]
for idx in range(2,41):
    fibo.append([fibo[idx-1][0]+fibo[idx-2][0], fibo[idx-1][1]+fibo[idx-2][1]])

for _ in range(int(input())):
    print(*fibo[int(input())])

# 0 : 1,0
# 1 : 0,1
# 2 : 1,1
# 3 : 1,2
# 4 : 2,3