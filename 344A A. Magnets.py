number_of_magnets = int(input())
count = 1
prev = int(input())

for i in range(1, number_of_magnets):
    next=int(input())
    if prev != next:
        prev = next
        count += 1

print(count)

