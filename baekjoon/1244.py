from sys import stdin

N = int(stdin.readline())
switch = list(map(int, stdin.readline().split()))
people_num = int(stdin.readline())
acts = list()
for _ in range(people_num):
  acts.append(list((map(int, stdin.readline().split()))))


def ans():
  for act in acts:
    if act[0] == 1:
      for idx, certain_switch in enumerate(switch):
        if (idx + 1) % act[1] == 0:
          switch[idx] = 1 if switch[idx] == 0 else 0
    else:
      standard=act[1]-1
      switch[standard] = 1 if switch[standard] == 0 else 0

      left, right = standard - 1, standard + 1

      while left >= 0 and right < len(switch):
        if switch[left] == switch[right]:
          switch[left] = switch[right] = 1 if switch[right] == 0 else 0
          left -= 1
          right += 1
        else :
          break


ans()
cut_list=list()
start=0
while True:
  if len(switch)>=20:
    cut_list.append(switch[0:20])
    switch=switch[20:]
  else:
    cut_list.append(switch)
    break

for part in cut_list:
  print(' '.join(map(str,part)))