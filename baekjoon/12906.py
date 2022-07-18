from sys import stdin
from collections import deque


def sol():

    A, B, C = [], [], []

    disk = [A, B, C]

    for i in range(3):
        s = stdin.readline().split()

        if s[0] == "0":
            disk[i] = ""
            continue
        else:
            disk[i] = s[1]

    for i in range(3):
        temp = disk[i][:]

        while temp and temp[0] == ["A", "B", "C"][i]:
            temp = temp[1:]

        disk[i] = temp[:]

    q = deque()

    q.append((*disk, 0))
    visit = set()
    visit.add((disk[0], disk[1], disk[2]))

    while q:
        a, b, c, count = q.popleft()

        # print(f"{a},{b},{c} count : {count}")

        if len(a) == 0 and len(b) == 0 and len(c) == 0:
            return count

        if len(a) > 0:
            color = a[-1]

            if color == "A":
                na = a[:-1]
                nb = b[:] + "A"
                nc = c[:]

                if not (na, nb, nc) in visit:
                    visit.add((na, nb, nc))
                    q.append((na, nb, nc, count + 1))

                na = a[:-1]
                nb = b[:]
                nc = c[:] + "A"

                if not (na, nb, nc) in visit:
                    visit.add((na, nb, nc))
                    q.append((na, nb, nc, count + 1))

            elif color == "B":
                # B가 아무것도 없으면, 그냥 버려도됨
                if len(b) == 0:
                    na = a[:-1]
                    nb = b[:]
                    nc = c[:]

                    if not (na, nb, nc) in visit:
                        visit.add((na, nb, nc))
                        q.append((na, nb, nc, count + 1))
                # B위에 뭐가 있으면 그대로 얹기
                else:
                    na = a[:-1]
                    nb = b[:] + "B"
                    nc = c[:]

                    if not (na, nb, nc) in visit:
                        visit.add((na, nb, nc))
                        q.append((na, nb, nc, count + 1))

                    na = a[:-1]
                    nb = b[:]
                    nc = c[:] + "B"

                    if not (na, nb, nc) in visit:
                        visit.add((na, nb, nc))
                        q.append((na, nb, nc, count + 1))
            else:
                # C가 아무것도 없으면, 그냥 버려도됨
                if len(c) == 0:
                    na = a[:-1]
                    nb = b[:]
                    nc = c[:]

                    if not (na, nb, nc) in visit:
                        visit.add((na, nb, nc))
                        q.append((na, nb, nc, count + 1))
                # B위에 뭐가 있으면 그대로 얹기
                else:
                    na = a[:-1]
                    nb = b[:]
                    nc = c[:] + "C"

                    if not (na, nb, nc) in visit:
                        visit.add((na, nb, nc))
                        q.append((na, nb, nc, count + 1))

                    na = a[:-1]
                    nb = b[:] + "C"
                    nc = c[:]

                    if not (na, nb, nc) in visit:
                        visit.add((na, nb, nc))
                        q.append((na, nb, nc, count + 1))

        if len(b) > 0:
            color = b[-1]

            if color == "B":
                na = a[:] + "B"
                nb = b[:-1]
                nc = c[:]

                if not (na, nb, nc) in visit:
                    visit.add((na, nb, nc))
                    q.append((na, nb, nc, count + 1))

                na = a[:]
                nb = b[:-1]
                nc = c[:] + "B"

                if not (na, nb, nc) in visit:
                    visit.add((na, nb, nc))
                    q.append((na, nb, nc, count + 1))

            elif color == "A":
                # A가 아무것도 없으면, 그냥 버려도됨
                if len(a) == 0:
                    na = a[:]
                    nb = b[:-1]
                    nc = c[:]

                    if not (na, nb, nc) in visit:
                        visit.add((na, nb, nc))
                        q.append((na, nb, nc, count + 1))
                # A위에 뭐가 있으면 그대로 얹기
                else:
                    na = a[:] + "A"
                    nb = b[:-1]
                    nc = c[:]

                    if not (na, nb, nc) in visit:
                        visit.add((na, nb, nc))
                        q.append((na, nb, nc, count + 1))

                    na = a[:]
                    nb = b[:-1]
                    nc = c[:] + "A"

                    if not (na, nb, nc) in visit:
                        visit.add((na, nb, nc))
                        q.append((na, nb, nc, count + 1))

            else:
                # C가 아무것도 없으면, 그냥 버려도됨
                if len(c) == 0:
                    na = a[:]
                    nb = b[:-1]
                    nc = c[:]

                    if not (na, nb, nc) in visit:
                        visit.add((na, nb, nc))
                        q.append((na, nb, nc, count + 1))
                # B위에 뭐가 있으면 그대로 얹기
                else:
                    na = a[:]
                    nb = b[:-1]
                    nc = c[:] + "C"

                    if not (na, nb, nc) in visit:
                        visit.add((na, nb, nc))
                        q.append((na, nb, nc, count + 1))
                    na = a[:] + "C"
                    nb = b[:-1]
                    nc = c[:]

                    if not (na, nb, nc) in visit:
                        visit.add((na, nb, nc))
                        q.append((na, nb, nc, count + 1))
        if len(c) > 0:
            color = c[-1]
            if color == "C":
                na = a[:] + "C"
                nb = b[:]
                nc = c[:-1]

                if not (na, nb, nc) in visit:
                    visit.add((na, nb, nc))
                    q.append((na, nb, nc, count + 1))

                na = a[:]
                nb = b[:] + "C"
                nc = c[:-1]

                if not (na, nb, nc) in visit:
                    visit.add((na, nb, nc))
                    q.append((na, nb, nc, count + 1))

            elif color == "A":
                # A가 아무것도 없으면, 그냥 버려도됨
                if len(a) == 0:
                    na = a[:]
                    nb = b[:]
                    nc = c[:][:-1]

                    if not (na, nb, nc) in visit:
                        visit.add((na, nb, nc))
                        q.append((na, nb, nc, count + 1))
                # A위에 뭐가 있으면 그대로 얹기
                else:
                    na = a[:] + "A"
                    nb = b[:]
                    nc = c[:-1]

                    if not (na, nb, nc) in visit:
                        visit.add((na, nb, nc))
                        q.append((na, nb, nc, count + 1))

                    na = a[:]
                    nb = b[:] + "A"
                    nc = c[:-1]

                    if not (na, nb, nc) in visit:
                        visit.add((na, nb, nc))
                        q.append((na, nb, nc, count + 1))
            else:
                # B가 아무것도 없으면, 그냥 버려도됨
                if len(b) == 0:
                    na = a[:]
                    nb = b[:]
                    nc = c[:-1]

                    if not (na, nb, nc) in visit:
                        visit.add((na, nb, nc))
                        q.append((na, nb, nc, count + 1))
                # B위에 뭐가 있으면 그대로 얹기
                else:
                    na = a[:]
                    nb = b[:] + "B"
                    nc = c[:-1]

                    if not (na, nb, nc) in visit:
                        visit.add((na, nb, nc))
                        q.append((na, nb, nc, count + 1))

                    na = a[:] + "B"
                    nb = b[:]
                    nc = c[:-1]

                    if not (na, nb, nc) in visit:
                        visit.add((na, nb, nc))
                        q.append((na, nb, nc, count + 1))


print(sol())
