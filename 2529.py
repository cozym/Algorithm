# 부등호
import sys

k = int(sys.stdin.readline())
sign = list(map(str,sys.stdin.readline().split()))
ans_max = 0
ans_min = 0
used_nums = [False for i in range(10)]
sequence = ""

# 재귀로 문자열 하나씩 만들면서 부등호에 어긋나면 out
# 부등호에 성립하며 k+1길이 완성되면 max, min값 비교
def make_sign(count):
    if count==k+1:
        return
    for i in range(10):
        if used_nums[i]:
            continue
        used_nums[i] = True
        sequence
        
print(k,sign)