#효울적인 코드(시간초과X)
def josephus(N, K):
    answer = []
    current = 0
    lst = [i for i in range(1, N+1)]
    while len(lst):
        current += K-1
        current %= len(lst)
        answer.append(str(lst.pop(current)))
    return answer

N, K = map(int, input().split())
print(josephus(N, K))
print("<", ", ".join(josephus(N, K)), ">")


""""처음 시도(시간초과)
def josephus(N, K):
    answer = []
    current = 0
    lst = [i for i in range(1, N+1)]
    while len(lst[current:]) != 1:
        if (current+1)%K == 0:
            answer.append(str(lst[current]))
        else:
            lst.append(str(lst[current]))
        current += 1
    answer.append(str(lst[current]))
    return answer

N, K = map(int, input().split())
print("<", ", ".join(josephus(N, K)), ">", sep='')
"""




