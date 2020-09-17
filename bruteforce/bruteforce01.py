# https://www.acmicpc.net/step/22
# https://www.acmicpc.net/problem/2798
N,M = input().split()
numbers = input().split()
temp = 0
almost = 0

for i in range(0,len(numbers)):
    for j in range(0,len(numbers)):
        for k in range(0,len(numbers)):
            if i == j or i == k or j == k:
                pass
            else:
                temp  = int(numbers[i]) + int(numbers[j]) + int(numbers[k])
                if temp > int(M) :
                    pass
                elif temp < int(M) and temp < almost:
                    pass
                else:
                    almost = temp
print(almost)

