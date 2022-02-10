#덱을 사용하고, 시간복잡도가 O(1)이어야함
import sys
from collections import deque
lst = deque([])
front_index = 0
testcase = int(input())
for _ in range(testcase):
    command = list(sys.stdin.readline().split())
    if command[0] == "push_front":
        lst.appendleft(int(command[1]))
    elif command[0] == "push_back":
        lst.append(int(command[1]))
    elif command[0] == "pop_front":
        if len(lst): print(lst.popleft())
        else: print(-1)
    elif command[0] == "pop_back":
        if len(lst): print(lst.pop())
        else: print(-1)
    elif command[0] == "size":
        print(len(lst))
    elif command[0] == "empty":
        if len(lst) == 0: print(1)
        else: print(0)
    elif command[0] == "front":
        if len(lst): print(lst[0])
        else:print(-1)
    elif command[0] == "back":
        if len(lst): print(lst[-1])
        else:print(-1)

