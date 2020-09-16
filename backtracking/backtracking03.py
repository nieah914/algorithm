# https://www.acmicpc.net/problem/15651

in_data = input()
N = int(in_data.split(' ')[0])
M = int(in_data.split(' ')[1])
validation = [False]*N
Array =[0]*M
# 4 2

def dfs(N,M,D) :
    if D == M:
        for i in range(0,M):
            print(str(Array[i]) + ' ' if i != len(Array) else'\n',end='')
        print()
        return

    for i in range(0 ,N):
        Array[D] = i + 1
        dfs(N,M,D+1)

dfs(N,M,0)