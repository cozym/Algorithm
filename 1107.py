# 리모컨
import sys

N = int(sys.stdin.readline())
d = int(sys.stdin.readline())
dead_nums = []
if d!=0:
    dead_nums = list(map(str,sys.stdin.readline().split()))
res = 1000000   # 정답에는 최솟값이 들어가므로 최댓값으로 초기설정
Immediate = 0   # N과 가장 가까운 수 저장

# 고장난 번호들이 들어가지 않은 수 중 N과 가장 가까운 수 찾기
for j in range(1000001):
    for k in dead_nums:
        if k in str(j):
            break
    else:
        if res > abs(N-j):
            Immediate = j
            res = abs(N-j)

res += len(str(Immediate))  # 찾아낸 N과 가장 가까운 수의 길이 더해주기

if abs(N-100) < res:    # 숫자버튼보다 +,-버튼 사용이 짧은 경우
    res = abs(N-100)

print(res)