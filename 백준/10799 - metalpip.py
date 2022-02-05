lst = list(input())
count = 0
range_metal = 0
i = 0
while i < len(lst):
    if lst[i] == "(":
        if lst[i+1] == ")": #레이저의 경우
            count += range_metal #범위에 있는 쇠들만큼 더한다(두배가 되기때문)
            i += 1 #레이저 인덱스를 넘어가기 위함
        else:
            count += 1 #레이저가 아닌 경우 새로운 막대가 쌓이는것
            range_metal += 1
    else:
        range_metal -= 1 #범위 내의 쇠막대가 하나 줄어드는것
    i += 1
print(count)

