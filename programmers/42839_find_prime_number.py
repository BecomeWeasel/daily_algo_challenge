from itertools import permutations


def solution(numbers):
    answer = 0
    numbers = list(numbers)

    len_numbers = len(numbers)

    # numbers가 N자리면 10^N-1까지 소수체크를 해줌
    is_prime = [True for i in range(10 ** (len_numbers))]
    is_prime[0] = is_prime[1] = False
    for i in range(2, int((10 ** (len_numbers)) ** 0.5)):
        if is_prime[i]:
            for j in range(i + i, 10 ** (len_numbers), i):
                is_prime[j] = False

    prime_set = set()

    # 순열에서 뽑는 개수를 1개에서부터 문자열의 개수만큼
    for i in range(1, len_numbers + 1):
        # 순열로 i개 만큼 뽑음
        for selected_numbers in permutations(numbers, i):
            # 뽑은 숫자가 소수인지 판별
            # 소수가 중복해서 뽑힐수가 있으니 체크해야함
            num = int("".join(selected_numbers))
            if is_prime[num] and not num in prime_set:
                prime_set.add(num)
                answer += 1

    return answer


if __name__ == "__main__":
    print(solution("011"))
