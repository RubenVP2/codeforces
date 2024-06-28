n = int(input())
count = 0
for i in range(0, n):
    text = str(input())
    if text.count("1") >= 2:
        count += 1
print(count)