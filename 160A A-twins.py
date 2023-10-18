number_Of_Coins = int(input())

coins = list(map(int, input().strip().split()))
coins.sort(reverse=True)

total = sum(coins)

seized_coins_sum = 0
counted_coin = 0

for i in coins:
    seized_coins_sum += i
    counted_coin += 1
    if seized_coins_sum > (total - seized_coins_sum):
        break

print(counted_coin)