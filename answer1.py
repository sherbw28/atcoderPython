import sys
input = sys.stdin.readline
n,q = map(int,input().split())
num = list(range(1, n + 1))
for _ in range(q):
    n = int(input())
    where = num.index(n)
    if where == len(num) - 1:
        num[where] = num[where - 1]
        num[where - 1] = n
    else:
        num[where] = num[where + 1]
        num[where + 1] = n
for item in num:
    print(item,end=" ")