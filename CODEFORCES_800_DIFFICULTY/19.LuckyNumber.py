n = input()
t=0
if '4' in n or '7' in n:
    for c in n:
        if c == "4" or c == "7":
            t+=1
    if t == 4 or t == 7:
        print('YES')
        exit()
    print("NO")
else:
    print("NO")