import sys

word = []   # 단어스택
bracket = 0 # 꺽쇠 표시
line = sys.stdin.readline().strip()

for i in range(len(line)):
    if line[i] == '<':
        bracket = 1     # 꺽쇠를 만나면 표시
        while word:     # 이전까지의 스택 역출력 및 스택비움
            print(word.pop(),end='')
        print('<',end='')
    elif line[i] == '>':
        print('>',end='')
        bracket = 0     # 꺽쇠가 끝나면 표시
    elif bracket == 1:  # 꺽쇠가 끝날 때 까지 그냥 출력
        print(line[i],end='')        
    elif line[i] == ' ':    # 공백을 만나면 스택 역출력 및 비움
        while word:
            print(word.pop(),end='')
        print(' ',end='')
    else:
        if bracket == 0:    # 꺽쇠 외부일 경우만 스택에 push
            word.append(line[i])
        if i == len(line)-1:    # 마지막 스택 역출력
            while word:
                print(word.pop(),end='')