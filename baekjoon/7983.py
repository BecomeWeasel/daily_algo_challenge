from sys import stdin

N = int(stdin.readline())

info = {i: [] for i in range(N)}

max_due, cons, ret = 0, 0, 0

for i in range(N):
    d, t = map(int, stdin.readline().split())
    info[i] = (d, t)

    max_due = max(max_due, t)

info = [(info[k][0], info[k][1], k) for k in range(N)]


info.sort(key=lambda x: -x[1])
cursor = max_due

for _, e in enumerate(info):
    d, t, number = e
    cursor = min(cursor, t)
    cursor = cursor - d

print(cursor)
