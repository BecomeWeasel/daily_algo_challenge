from sys import stdin

# 같은 구성 체크하는 방법 => 단어내 알파벳 정렬후 비교 ?

N = int(stdin.readline())
standard = stdin.readline().rstrip("\n")
words = [stdin.readline().rstrip("\n") for _ in range(N - 1)]


def ans():
    result = len(words)
    standard_counter = [0 for _ in range(26)]

    for char in standard:
        standard_counter[ord(char) - 65] += 1

    for word in words:

        # 무조건 안되는 경우 => 길이가 2이상 차이나는 경우
        if abs(len(word) - len(standard)) > 1:
            result -= 1
            continue

        # 비슷한 단어 체크하는 방법 => 알파벳 단어들이 각각 몇개 있는지 체크한후 각 알파벳마다 차이가 1이하인것만 비슷한 단어
        word_counter = [0 for _ in range(26)]

        for char in word:
            word_counter[ord(char) - 65] += 1

        differ = sum((abs(a - b) for a, b in zip(standard_counter, word_counter)))

        # 다른것이 두개까지는 괜찮은데, 그 이유는 ABA : ACA라면 원문의 B가 ACA는 없으니 differ가 1이 생기고, ACA의 C가 원문에는 없으니 differ가 1이 추가되니 2까지는 괜찮다.
        if differ > 2:
            result -= 1

    return result


print(ans())
