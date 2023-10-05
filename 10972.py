# 다음 순열
import sys
import itertools

N = int(sys.stdin.readline())
compare = list(map(int,sys.stdin.readline().split()))

# itertools를 사용하여 다음 순열 출력
if compare == sorted(compare,reverse=True):
    print(-1)
else:
    ans = list(itertools.permutations(compare))[1]
    print(*ans)