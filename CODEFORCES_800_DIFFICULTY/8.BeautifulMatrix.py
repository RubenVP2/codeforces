li = [list(map(int, input().split())) for _ in range(5)]
for i in range(5):
    for j in range(5):
        if li[i][j] == 1:
            x, y = i, j
            break
print(abs(x-2) + abs(y-2))