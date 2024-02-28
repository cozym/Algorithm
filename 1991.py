# 트리 순회
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

tree = {}

for _ in range(int(input())):
    parent,left,right = map(str,input().split())
    tree[parent] = [left,right]

def preOrder(node):
    print(node,end='')
    if tree[node][0] != '.':
        preOrder(tree[node][0])
    if tree[node][1] != '.':
        preOrder(tree[node][1])

def inOrder(node):
    if tree[node][0] != '.':
        inOrder(tree[node][0])
    print(node,end='')
    if tree[node][1] != '.':
        inOrder(tree[node][1])

def postOrder(node):
    if tree[node][0] != '.':
        postOrder(tree[node][0])
    if tree[node][1] != '.':
        postOrder(tree[node][1])
    print(node,end='')

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')