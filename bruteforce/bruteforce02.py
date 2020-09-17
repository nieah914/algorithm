# https://www.acmicpc.net/step/22
# https://www.acmicpc.net/problem/2231


def serialSum(input):
    tesxtInput = str(input)
    result = 0
    for i in range(0,len(str(input))):
        result = result + int(tesxtInput[i])
    return result


M = int(input())

result = 0
for i in range(0,M):
    if serialSum(i) + i  == M:
        result = i
        break
print(result)