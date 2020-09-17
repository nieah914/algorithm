# 알고리즘 - DFS - (1/50) - 백준15649
# https://www.acmicpc.net/problem/15649
inputs = input()
N = int(inputs.split(' ')[0])
M = int(inputs.split(' ')[1])
arr = []
visit = []
for i in range(0,N):
    visit.append(False)

for i in range(0,M):
    arr.append('')


def dfs(n, m, d):
    if d == m:
        for i in range(0, m):
            print(str(arr[i]) + ' ' if i != len(arr) else'', end='')
        print()
        return
    for i in range(0,n):
        if visit[i] == False:
            visit[i] = True
            arr[d] = i+1
            dfs(n,m,d+1)
            visit[i] = False

dfs(N,M,0)

