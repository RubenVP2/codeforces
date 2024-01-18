#Nb d'arret
n = int(input())
#Nb minimum
m = 0
for i in range(n):
    temp = 0
    # nb de personne sortante / entrante
    p = list(map(int, input().split()))
    temp -= p[0]
    temp += p[1]
    if i == 0:
        m = temp
    if temp > m:
        m = temp
print(m)