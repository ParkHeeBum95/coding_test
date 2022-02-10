import sys
from collections import Counter

N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
count_lst = Counter(lst) #등장횟수를 정리해놓은 dic

answer = [-1] * N #디폴트를 -1로 걸어놓은 리스트
stack = [] #현재 가르키는 인덱스를 저장해놓을 스택
stack.append(0)
for i in range(1, N):
    while stack and count_lst[lst[stack[-1]]] < count_lst[lst[i]]:
        answer[stack.pop()] = lst[i]
    stack.append(i)
print(*answer)



