# 부등호
import sys

k = int(sys.stdin.readline())
sign = list(map(str,sys.stdin.readline().split()))
ans_max = []
ans_min = []
used_nums = [False for i in range(10)]
sequence = [0 for i in range(k+1)]

# 재귀로 문자열 하나씩 만들면서 부등호에 어긋나면 out (백트래킹, 탐색시간 감소)
# 부등호에 성립하며 k+1길이 완성되면 max, min값 비교
def make_sign(count):
    if count==k+1:
        global ans_min
        global ans_max
        if len(ans_min) == 0:   # 오름차순이기에 첫 리스트를 min에 저장
            ans_min = sequence[:]
        ans_max = sequence[:]   # 마지막 리스트를 max에 저장
        return
    for i in range(10):
        if used_nums[i]:
            continue
        used_nums[i] = True
        sequence[count] = i
        if not check_sign(sequence,count):  # 앞부분에서 부등호 성립 안할 경우 뒷부분 검사 x
            used_nums[i] = False
            continue
        make_sign(count+1)
        used_nums[i] = False
        
# 부등호 성립 확인
def check_sign(s,c):
    if c==0:
        return True
    if sign[c-1] == '>':
        return s[c-1] > s[c]
    elif sign[c-1] == '<':
        return s[c-1] < s[c]

make_sign(0)
print(''.join(map(str,ans_max)))
print(''.join(map(str,ans_min)))