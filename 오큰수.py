N = int(input(""))
seq = list(map(int,input().split()))
nge_index = []
L = len(seq)
result = [-1 for i in range(L)]

### 시간 초과 ###
# for i in range(L):
#     for j in range(i,L):
#         if(seq[i] < seq[j]):
#             print(seq[j],end=" ")
#             break
#         elif j==L-1:
#             print(-1,end=" ")

for i in range(L):
    if(nge_index):
        while(nge_index and seq[i] > seq[nge_index[-1]]):
            result[nge_index.pop()] = seq[i]
        nge_index.append(i)
    else:
        nge_index.append(i)

print(*result)