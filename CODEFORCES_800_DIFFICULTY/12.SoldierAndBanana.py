x = list(map(int, input().split()))
total = 0
for i in range(1, x[2] + 1):
    total += i * x[0]
print(total - x[1] if total - x[1] > 0 else 0)
