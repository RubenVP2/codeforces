x = list(map(int, input().split()))
i = 0
while True:
    if x[0] <= x[1]:
        x[0] *= 3
        x[1] *= 2
        i += 1
        continue
    break
print(i)