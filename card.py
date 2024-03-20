import sys

cards = ["A", "C", "BA", "B", "BB", "BAC", "D"]
# result = [1,1,2,3,2]
#cards = ["Z","Y","X","W","WW","WWW","WWWW","WWWW"]
# result = [1,2,3,4,4,4,4]

answer = []
res = []

for idx,card in enumerate(cards):
    for j in range(len(answer)): # 사슬이 n개일 때 모든 사슬 검사
        if answer[j][-1] < card:    # 사슬의 마지막에 있는 카드와 사전순 비교
            answer[j].append(card)  # 사전순으로 뒤에 온다면 추가
            res.append(j+1)         # 현재 카드가 어느 사슬에 들어가는지 res에 추가
            break
    else:
        answer.append([card])  # 사슬을 다 돌고도 추가할 곳이 없으면 새로운 사슬을 추가
        res.append(len(answer))  # 현재 카드가 어느 사슬에 들어가는지 res에 추가

print(res)