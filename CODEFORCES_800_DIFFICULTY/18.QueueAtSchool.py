n,t = map(int, input().split())
sQueue = input()
for sec in range(t):
    flag = False
    for i in range(n):
        if flag: 
            flag = False
            continue
        if sQueue[i] == "B" and i != n -1 and sQueue[i+1] == "G":
            sQueue = sQueue[:i] + sQueue[i+1] + sQueue[i] + sQueue[i+2:]
            flag = True
print(sQueue)