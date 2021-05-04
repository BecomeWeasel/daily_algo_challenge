from sys import stdin

N = int(stdin.readline())


def sol():

    words = list()

    for _ in range(N):
        words.append(stdin.readline().rstrip())

    words = list(set(words))


    for word in sorted(words, key=lambda x: (len(x),x)):
        print(word)


sol()