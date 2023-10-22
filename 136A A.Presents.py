numer_of_friends = int(input())
friends = list(map(int, input().strip().split()))

ans = [0] * len(friends)
for i in range(numer_of_friends):
    ans[friends[i]-1] = i + 1

print(*ans)




