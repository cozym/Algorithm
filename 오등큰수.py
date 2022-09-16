import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int,sys.stdin.readline().rsplit()))
F = {}
result = [-1 for i in range(N)]
NGF = []

for i in A:
    if i in F:
        F[i] += 1
    else:
        F[i] = 1

#NGF.append(A[0])
for i in range(N):
        while NGF and F[A[i]] > F[A[NGF[-1]]]:
            result[NGF.pop()] = A[i]
        NGF.append(i)

print(*result)

# [3,3,2,1,1,2,3]
# 해당 수를 +1
# 한바퀴 돌려서 각 위치의 빈도수 list추출
# 두바퀴째 스택을 사용하여 result 업데이트
# for i in range(N):
