from collections import defaultdict
d = defaultdict(list)
n,k = map(int,input().split())
for i in range(n):
    li = list(input())
    for item in li:
        d[item].append(i)
l = []
for i in range(2 ** n):
    bag = []
    for j in range(n):
        if((i >> j) & 1):
            bag.append(j)
    l.append(bag)
print(l)