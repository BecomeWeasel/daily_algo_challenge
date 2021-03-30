from sys import stdin
from collections import deque


def ans():
  cnt = 0

  bfs()

  for i in truth_party:
    if i == False:
      cnt += 1
  
  # 0번째파티(실제로 없는 파티)도 포함하니끼
  return cnt-1


def bfs():
  q = deque()
  for know_the_true in know_the_true_people:
    q.append((know_the_true))
    visited[know_the_true] = True
  while q:
    target = q.popleft()
    for i in range(1, M + 1):
      # target이 i번째 파티에 참여했다면
      # 그 파티에서는 진실을 말해야한다
      # 이미 진실로 바뀌었다면 탐색 필요 X (그전에 탐색완료)
      if people_party_connection[i][target] and not truth_party[i]:
        truth_party[i] = True
        # 이 파티에 참석한 사람들도
        # 진실을 들어야하니
        # 탐색해야한다
        for j in range(1, N + 1):
          if people_party_connection[i][j] and not visited[j]:
            q.append((j))


N, M = map(int, stdin.readline().split())
visited = [False for _ in range(N + 1)]
truth_party = [False for _ in range(M + 1)]

know_the_true_people = list(map(int, stdin.readline().split()))
# 맨 앞은 개수이니
know_the_true_people.pop(0)

# if know_the_true_people_cnt != 0:
#   for people in map(int, stdin.readline().split()):
#     know_the_true_people.append(people)

# people_party_connection[i][j] : 파티 i에 j가 참석했는지
people_party_connection = [[False] * (N + 1) for _ in range(M + 1)]

# party_participant = [[] for _ in range(M + 1)]

# # joined_party[i] : i번째 사람이 참석하는 파티번호
# joined_party = [[] for _ in range(N + 1)]
# for order in range(1, M + 1):
#   party_cnt = int(stdin.readline())
#   for _ in range(party_cnt):
#     people = int(stdin.readline())
#     party_participant[order].append(people)
#     joined_party[people].append(order)

for party_number in range(1, M + 1):
  participant_list = list(map(int, stdin.readline().split()))
  participant_list.pop(0)
  for i in range(len(participant_list)):
    people_party_connection[party_number][participant_list[i]] = True

print(ans())