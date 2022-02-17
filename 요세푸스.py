import sys

commend = sys.stdin.readline().split()
N , K = int(commend[0]),int(commend[1])
queue = list(map(int,range(1,int(N+1))))
output = []
pointer = 0

while(len(output)!=N):
    pointer = (pointer+(K-1))%len(queue)
    output.append(str(queue.pop(pointer)))

print('<'+", ".join(output)+'>')