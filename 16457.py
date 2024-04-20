# 단풍잎 이야기
<<<<<<< HEAD
=======
import sys
from itertools import combinations
input = sys.stdin.readline

n,m,k = map(int,input().split())
skills = [False for _ in range(2*n+1)]
questNeedSkill = []
res = 0

for _ in range(m):
    questNeedSkill.append(list(map(int,input().split())))

def countSolveQuest(skills):
    cnt = 0
    global res
    for s in range(m):
        if cnt+(m-s) < res:
            break
        for j in questNeedSkill[s]:
            if not skills[j]:
                break
        else:
            cnt += 1
    res = max(cnt, res)

mySkillSet = combinations(range(1,2*n+1),n)

for skillSet in mySkillSet:
    skills = [False for _ in range(2*n+1)]
    for i in skillSet:
        skills[i] = True
    countSolveQuest(skills[:])

print(res)
>>>>>>> 43672b1899370d93b1b4f66bb3c5d439f8daa6a8
