# 매직 스타
import sys
input = sys.stdin.readline

# 한줄 리스트로 검토
check = [4,10,12,14,16,20,24,28,30,32,34,40]
lines = [[4,12,20,28],[4,14,24,34],[10,12,14,16],[10,20,30,40],[16,24,32,40],[28,30,32,34]]
used = [False for _ in range(12)]
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L']
star = []
ans = []

for _ in range(5):
    l = input().rstrip()
    for i in l:
        if i in alpha:
            used[ord(i)-65] = True
        star.append(i)

def recur(idx,star,used):
    # 각 라인의 합 26 검사
    for line in lines:
        s = 0
        for p in line:
            if star[p] == 'x':  # 라인 검사 중 x나오면 스킵
                break
            s += (ord(star[p])-65+1)
        else:   
            if s != 26: # 중간에 x가 안나오고 라인 끝까지 검사했을때 합이 26이 아니면 반환
                return
            
    if idx == 12:
        ans.append(star)
        return
        
    if star[check[idx]] != 'x': # 체크 원소가 채워져있으면 스킵
        recur(idx+1,star[:],used[:])
    else: 
        for i in alpha:
            if used[ord(i)-65]:
                continue
            used[ord(i)-65] = True
            star[check[idx]] = i
            recur(idx+1, star[:], used[:])
            used[ord(i)-65] = False

recur(0,star[:],used[:])

ans.sort()

for e in range(45):
    print(ans[0][e],end='')
    if (e+1) % 9 == 0:
        print()

# 입력받고 이미 채워진 알파벳 제거
# 남아있는 알파벳으로 재귀
# 매직 스타 규칙에 맞는지 확인 > 맞지 않으면 return
# 마지막까지 맞는 경우 append