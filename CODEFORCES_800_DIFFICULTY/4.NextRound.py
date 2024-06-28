nK = input()
k = int(nK.split(" ")[1])
scores = input().split()
count = 0
for scr in scores:
    if int(scr) > 0 and int(scr) >= int(scores[k - 1]):
        count += 1
print(count)