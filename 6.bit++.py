n = int(input())
res = 0
for i in range(n):
    s = input()
    if '+' in s:    
        res += 1
    else:
        res -= 1
print(res) 