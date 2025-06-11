import sys
sys.stdin, sys.stdout = open("helpcross.in", "r"), open("helpcross.out", "w")
c, n = list(map(int,input().split()))
chickens = []
cow_times = []
pairs = 0
used = set()


def binary(value, list):
    l, r = 0, len(list) - 1
    while l <= r:
        mid = (r-l+1)//2 + 1
      
        if list[mid] >= value:
            r = mid-1
        else:
            l = mid+1
    
    return l


for i in range(c):
    chickens.append(int(input()))

for _ in range(n):
    x, y = input().split()
    cow_times.append((int(x), int(y)))

chickens.sort()
cow_times.sort(key=lambda x: x[1])

for x in cow_times:
    idx = binary(x[0], chickens)
    if idx <= x[1]:
        pairs += 1
        chickens.pop(idx)
    

print(pairs)