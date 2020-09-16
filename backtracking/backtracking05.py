# https://www.acmicpc.net/problem/9663

N = int(input())
visit = []
for i in range(0,N):
    temp = []
    for j in range(0,N):
        temp.append(False)
    visit.append(temp)

def solve(N):
    # 행
    for i in range(0,N):
        # 열
        for j in range(0,N):
            if visit[i][j] == False:
                for x in range(0,N):
                    for y in range(0,N):
                        visit[i][j] = True