x = int(input())
c = 0
p = 0
for i in range(x):
    n,m=list(map(int, input().split()))
    p += m - n
    c = max(c, p)
print(c)
