# https://www.acmicpc.net/step/22
# https://www.acmicpc.net/problem/9663



N = int(input())
cost_days   = []
earn_moneys = []
total_cost = 0

def cal(i , cost):
    if i > N-1:
        return
    global total_cost
    if total_cost <= cost:
        total_cost = cost
    else:
        pass

    if i + cost_days[i] - 1 <= N:
        cost = cost + earn_moneys[i]
        cal(i+1,cost)
    else:
        return
    cal(i+1,cost)



for i in range(0,N):
    raw = input().split(' ')
    cost_days.append(int(raw[0]))
    earn_moneys.append(int(raw[1]))

cal(0,0)
print(total_cost)


