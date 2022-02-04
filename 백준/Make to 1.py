N = int(input())
count = 0
while True:
    if N == 1:
        break
    count += 1
    if N % 3 == 0:
        N /= 3
        continue
    elif N % 2 == 0:
        N /= 2
        continue
    else:
        N -= 1
        continue
print(count)
