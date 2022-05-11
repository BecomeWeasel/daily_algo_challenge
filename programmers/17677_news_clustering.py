from collections import Counter


def isValid(c):
    alpha = {
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    }

    return c in alpha


def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()

    a = list()
    b = list()

    len_1 = len(str1)
    len_2 = len(str2)

    str1 = list(str1)
    str2 = list(str2)

    try:
        for i in range(len(str1) - 1):
            if isValid(str1[i]) and isValid(str1[i + 1]):
                a.append("".join(map(str, str1[i : i + 2])))

        for i in range(len(str2) - 1):
            if isValid(str2[i]) and isValid(str2[i + 1]):
                b.append("".join(map(str, str2[i : i + 2])))
    except:
        print(5)
    c1 = Counter(a)
    c2 = Counter(b)

    hat = list((c1 & c2).elements())
    cup = list((c1 | c2).elements())

    if len(hat) == 0 and len(cup) == 0:
        return 65536

    return int((len(hat) / len(cup)) * 65536)
