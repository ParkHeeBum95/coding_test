glass_num = int(input()) # 총 포도잔의 수
glasses = [0] #n번 포도잔에 담긴 포도주의 양
for i in range(glass_num):
    glasses.append(int(input()))
dp = [0, glasses[1]]
if glass_num > 1:
    dp.append(glasses[1] + glasses[2])
for i in range(3, glass_num+1):
    dp.append(max(dp[i-3]+glasses[i-1]+glasses[i], dp[i-2]+glasses[i], dp[i-1]))
print(dp[glass_num])