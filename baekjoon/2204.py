from sys import stdin


def ans():
    words = list()
    for _ in range(N):
        words.append(str(stdin.readline().rstrip("\n")))

    upper_words = list()
    for idx, item in enumerate(words):
        upper_words.append([item.upper(), idx])
    upper_words.sort()

    return words[upper_words[0][1]]


N = -1
while True:
    N = int(stdin.readline())
    if N == 0:
        break
    print(ans())
