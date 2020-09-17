# https://www.acmicpc.net/step/22
# https://www.acmicpc.net/problem/1436

N = int(input())
i = 666
cnt = 0
while True:
    num_str = str(i)
    for j in range(0, len(num_str)-2):
        if str(i)[j:j+3] == '666':
            cnt = cnt + 1
            break
    if cnt == N:
        break
    else:
        i = i + 1
print(str(i))

