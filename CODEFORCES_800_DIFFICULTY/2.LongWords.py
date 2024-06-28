n = int(input())
for i in range(0, n):
    word = str(input())
    n = len(word)
    if n > 10:
        print(word[0] + str(n - 2) + word[n - 1])
    else:
        print(word)