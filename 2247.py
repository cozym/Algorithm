# 실질적 약수
import sys
input = sys.stdin.readline

n = int(input())
res = 0

# n//2보다 큰 SOD는 존재x
# n//2까지 증가시키며 i*n//2 -1 더해주기
for i in range(2,int(n//2)+1):
    res += i*((n//i)-1)
    res %= 1000000

print(res%1000000)

# 1 2 3 4 5 6 7 8 9 10 11 12 13
#   2   2   2   2   2     2     > 13//2 = 6 - 1
#     3     3     3       3     > 13//3 = 4
# .
# .
# .
#                         12    > 13//2 = 1
#                            13 > 