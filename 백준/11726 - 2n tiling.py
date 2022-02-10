# n (n-2k)(n-2k+1) n-2k
n = int(input())
answer = [None, 1,2,3]

for i in range(4, 1001):

    answer.append(answer[i-1]+answer[i-2])
print(answer[n] % 10007)
