n = int(input())
isOk = False
for i in range(2, n):
    if i % 2 == 0 and (n - 2) % 2 == 0:
        isOk = True
        break

if isOk:
    print("YES")
else:
    print("NO")
