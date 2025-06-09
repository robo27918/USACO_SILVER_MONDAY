import sys
sys.stdin, sys.stdout = open("helpcross.in", "r"), open("helpcross.out", "w")
c, n = list(map(int,input().split()))
chickens = []
cow_times = []
pairs = 0
used = set()
for i in range(c):
    chickens.append(int(input()))

for _ in range(n):
    x, y = input().split()
    cow_times.append((int(x), int(y)))

chickens.sort()
cow_times.sort(key=lambda x: x[1])

for x in chickens:
    for y in cow_times:
        if x <= y[1] and y not in used:
            pairs += 1
            used.add(y)
            break

print(pairs)