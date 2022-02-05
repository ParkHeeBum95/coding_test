string = str(input())
temp = [] #문자열을 임시로 저장해주는 리스트
flag = 0 #괄호 안 인지 아닌지 flag
for i in range(len(string)):
    if string[i] == "<":
        #괄호 전의 temp 파일을 출력
        temp.reverse()
        print("".join(temp), end="")
        temp = []
        flag = 1
    if flag == 1: # 괄호에 들어상황
        if string[i] == ">":
            temp.append(string[i])
            flag = 0
            print("".join(temp),end="")
            temp = []
            continue
        temp.append(string[i])
    else: # 괄호에 들어있지 않은 상황
        if i == len(string)-1:
            temp.append(string[i])
            temp.reverse()
            print("".join(temp), end=" ")
        if string[i] == " ":
            temp.reverse()
            print("".join(temp), end=" ")
            temp = []
        else:
            temp.append(string[i])


