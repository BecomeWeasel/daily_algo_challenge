from sys import stdin
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]



def ans():
  global visit,move_cnt
  while True:
    visit=[[False]*N for _ in range(N)]
    # 한번도 이동이 없다는건
    # 이미 인구수 이동이 조절이 된것이므로
    # 이동을 멈춰야함
    entire_no_move = True

    for i in range(N):
      for j in range(N):
        if not visit[i][j]:
          this_not_move=bfs(i, j)

          # this_not_move가 false라는것은
          # 이번 루프에서 단 한 번이라도 인구수가 이동되었다는 의미로
          # entire_no_move가 False임
          if not this_not_move:
            entire_no_move=False

    # 이번 루프에서 전체 나라에서 
    # 한번도 이동이 일어나지 않았으면 종료해야함
    if entire_no_move: 
      break

    # 이번 루프때 전체 나라에서
    # 인구수 이동이 한번이라도 일어났다는것
    else :
      move_cnt+=1

  return move_cnt


def bfs(start_y, start_x):
  q = deque()
  total_people = A[start_y][start_x]
  nation_cnt = 1

  # 인구수가 조절되어야하는
  # 나라의 좌표를 저장
  after_move_q = deque()
  after_move_q.append((start_y, start_x))
  q.append((start_y, start_x))
  visit[start_y][start_x] = True

  while q:

    y, x= q.popleft()

    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]

      if ny < 0 or nx < 0 or ny >= N or nx >= N:
        continue

      if L <= abs(A[ny][nx] - A[y][x]) <= R and not visit[ny][nx]:
        # 나중에 인구수 업데이트를 하기 위해
        # 조정될 나라의 좌표를 저장
        after_move_q.append((ny, nx))
        total_people += A[ny][nx]
        nation_cnt += 1
        q.append((ny, nx))
        visit[ny][nx] = True

  # 연합된 나라의 평균 인구수
  # 소수점 절삭해야함
  avg_people = int(total_people / nation_cnt)

  while after_move_q:
    y, x = after_move_q.popleft()
    A[y][x] = avg_people

  # 조정될 인구수가 1개라면
  # 조정될 곳이 없다는 의미
  # 이번 탐색에서는 인구수 이동이 일어나지 않음
  if nation_cnt==1:
    return True
  else:
    return False
   

move_cnt = 0
N, L, R = map(int, stdin.readline().split())
A = [[0] * N for _ in range(N)]
visit = [[False] * N for _ in range(N)]

for i in range(N):
  A[i] = list(map(int, stdin.readline().split()))

print(ans())
