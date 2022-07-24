from sys import stdin

D, N = map(int, stdin.readline().split())

oven = list(map(int, stdin.readline().split()))

temp = [987654321 for _ in range(D + 1)]

# 어차피 각각 너비만 필요한게 아니라 지금까지 입력받은것중 제일 낮은 너비만필요함
# 왜냐면 나보다 더 좁은 너비가 있으면 나한테 못옴 ;;;
for idx, o in enumerate(oven):
    temp[idx + 1] = min(temp[idx], o)

oven = temp[:]

pizza = list(map(int, stdin.readline().split()))

# 모든 도우들에대해서
for p in pizza:
    # 뎁스 내려가면서
    # 피자반죽이 담길 위치를 찾음
    while D > 0 and oven[D] < p:
        D -= 1
    D -= 1


print(D + 1 if D >= 0 else 0)
