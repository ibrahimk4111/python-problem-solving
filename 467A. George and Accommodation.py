number_of_room = int(input())

count = 0

for _ in range(number_of_room):
    p,q = map(int, input().split())
    if(q-p)>= 2:
        count = count + 1

print(count)