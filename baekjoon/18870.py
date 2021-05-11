from sys import stdin

N = int(stdin.readline())


def sol():
    numbers = list(map(int, stdin.readline().split()))

    numbers_ = sorted(set(numbers))

    answer_dict = {v: i for i, v in enumerate(numbers_)}
    
    answer=list()
    
    for number in numbers:
        answer.append(answer_dict[number])
    
    print(' '.join(map(str,answer)))


sol()