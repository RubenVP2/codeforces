x = list(map(int, input().split()))
for i in range(x[1]):
    # permet de vérifier le dernier chiffre d'un nombre
    if x[0] % 10 != 0:
        x[0] -= 1
    else:
        x[0] //= 10
print(x[0])