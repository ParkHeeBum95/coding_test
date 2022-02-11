card_num = int(input())
dp = [0] * (card_num+1) # 전체 가격
prices = [0] + list(map(int, input().split())) #n개당 가격
dp[1] = prices[1] #1개일땐 같고,
dp[2] = max(prices[1]*2, prices[2]) #2개일때 또한 지정해줄 수 있다.

for i in range(3, card_num+1):
    for j in range(1, i+1):
        if dp[i] <= dp[i-j] + prices[j]:
            dp[i] = dp[i-j] + prices[j]  #최대값으로 갱신
print(dp[card_num])


