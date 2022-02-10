import sys
lst_len = int(input())
lst = list(map(int, sys.stdin.readline().split()))
answer = [-1] * lst_len
stack = []

stack.append(0)
for i in range(1, lst_len):
    while stack and lst[i] > lst[stack[-1]]:
        answer[stack.pop()] = lst[i]
    stack.append(i)
print(*answer)




"""
#시간초과
import sys
lst_len = int(input())
lst = list(map(int, sys.stdin.readline().split()))
answer = []
for i in range(lst_len):
    found = 0
    if i == lst_len-1:
        answer.append(str(-1))
        break
    for j in range(i+1, lst_len):
        if lst[i] < lst[j]:
            answer.append(str(lst[j]))
            found = 1
            break
    if found==0:
        answer.append(str(-1))
print(" ".join(answer))
"""
