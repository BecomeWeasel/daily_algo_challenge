from collections import deque
from sys import stdin


def ans():
  return bfs(s)


def bfs(S):
  q = deque()
  q.append((1, 0, 0))
  visited[1][0] = True
  while q:
    emoji, board, time = q.popleft()

    if emoji == S:
      return time

    # 클립보드에 저장
    if not visited[emoji][emoji]:
      q.append((emoji, emoji, time + 1))
      visited[emoji][emoji] = True

    # 붙여넣기
    if emoji + board <= S and not visited[emoji + board][board]:
      q.append((emoji + board, board, time + 1))
      visited[emoji + board][board] = True

    # 삭제하기

    if emoji - 1 >= 0 and not visited[emoji - 1][board]:
      q.append((emoji - 1, board, time + 1))
      visited[emoji - 1][board] = True


s = int(stdin.readline())
# visited[i][j] : 화면에 i개 있을때 클립보드에 j개 있을때
# 2차원인 이유는 1차원배열만 쓰면 클립보드에 저장하는 탐색을 할때
# 이미 i개의 이모티콘을 출력하는 행동일때 탐색되어있다고 체크를 하므로 (visited[i]==True)
# 클립보드로 복사하는 행동이 일어나지 않음 (L20)
# 그래서 현재 클립보드와 화면에 적힌 이모티콘의 개수로 2차원 방문배열을 만들어야함
# visited 배열의 차원은 탐색시 바뀌는 상황의 개수라고 인식
# 이 문제에서는 이모티콘의 개수와 클립보드에 있는 이모티콘의 개수가 상황 두개
visited = [[False] * (s + 1) for _ in range(s + 1)]
print(ans())