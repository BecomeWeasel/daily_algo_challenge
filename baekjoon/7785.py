from sys import stdin

N = int(stdin.readline())
co = dict()
for _ in range(N):
    name, door = map(str, stdin.readline().split())
    if door == "enter":
        co.update({name: True})
    elif door == "leave":
        co.update({name: False})

co = dict(sorted(co.items(), reverse=True))

for key in co.keys():
    if co[key] == True:
        print(key)
