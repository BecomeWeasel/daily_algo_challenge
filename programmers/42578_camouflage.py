from collections import defaultdict
from math import prod

def solution(clothes):
    answer = 1
    items = defaultdict(list)

    for e in clothes:
        items[e[1]].append(e[0])

    # 경우의 수는
    # 각각의 아이템에 대해서 안 끼거나 item의 개수만큼의 경우의 수를 가지고 있으니
    # 모두 곱한 뒤 아무것도 안끼는 경우의 수 1개를 빼주면 됨

    # items의 key들에 대해서 len(items[key])를 하면 
    # key 종류의 아이템들의 개수가 나옴, 착용안하는 경우 1을 더해주고
    # prod 안 iterable은 옷 종류별 개수+1
    # prod 로 모두 곱함

    return prod(list(map(lambda x : len(items[x])+1, items)))-1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	))