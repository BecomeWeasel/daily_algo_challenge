from functools import cmp_to_key

def cmp(a,b):
    if int(str(a)+str(b))>int(str(b)+str(a)):
        return -1
    else:
        return 1

def solution(numbers):
    answer = ''
    numbers=sorted(numbers,key=cmp_to_key(cmp))
    for num in numbers:
        answer+=str(num)
    # 억지스러운 부분이 있다. 
    return str(int(answer))