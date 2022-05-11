from collections import deque


def is_convertible(origin, dest):
    diff = 0

    for idx, char in enumerate(list(origin)):
        if char != list(dest)[idx]:
            diff += 1

    return True if diff <= 1 else False


def solution(begin, target, words):
    answer = 0

    # words 안에 target이 없을때
    # 즉시 종료해야함
    is_exist_in_words = False

    for word in words:
        if word == target:
            is_exist_in_words = True

    if not is_exist_in_words:
        return answer

    q = deque()
    q.append((begin, 0, [False for _ in range(len(words))]))

    while len(q) != 0:
        origin, count, visit = q.popleft()

        if origin == target:
            answer = count
            break

        for idx, word in enumerate(words):
            if is_convertible(origin, word) and not visit[idx]:
                visit[idx] = True
                q.append((word, count + 1, visit))

    return answer


if __name__ == "__main__":
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
