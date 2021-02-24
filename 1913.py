from sys import stdin


def ans():
  grid = [[0 for _ in range(N)] for _ in range(N)]

  posx, posy = 0, 0
  direct = 0

  dy = [1, 0, -1, 0]
  dx = [0, 1, 0,-1 ]

  for num in range(N**2, 0, -1):
    grid[posy][posx] = num

    nposy, nposx = posy + dy[direct], posx + dx[direct]

    # 다음 방향이 이미 방문했거나 범위를 초과했으면
    # 반시계방향으로 방향을 돌려서 숫자를 기록
    if  nposy>=N or nposx>=N or nposy<0 or nposx<0 or grid[nposy][nposx]!=0:
      direct=(direct+1)%4
      nposy, nposx = posy + dy[direct], posx + dx[direct]
    
    posy,posx=nposy,nposx

  for i in range(N):
    for j in range(N):
      grid[i][j] = str(grid[i][j])

  for i in range(N):
    print(" ".join(grid[i]))

  for i in range(N):
    for j in range(N):
      if int(grid[i][j])==NN:
        print(str(i+1)+ " "+str(j+1))
  return N


N = int(stdin.readline())
NN = int(stdin.readline())
ans()