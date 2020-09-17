# https://www.acmicpc.net/step/22
# https://www.acmicpc.net/problem/7568

N = int(input())
height = []
weight = []
rank   = []

for i in range(0, N):
    temp = input().split()
    height.append(temp[0])
    weight.append(temp[1])
    rank.append(1)

for i in range(0,N):
    cnt = 0
    for j in range(0,N):
        if i == j:
            pass
        else:
            if height[i] < height[j] and weight[i] < weight[j]:
                cnt = cnt + 1
    rank[i] = cnt + 1
for i in range(0,N):
    if i == 0:
        pass
    else :
        print(' ',end='')
    print(str(rank[i]),end='')