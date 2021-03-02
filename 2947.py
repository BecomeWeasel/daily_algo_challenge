from sys import stdin


def ans(pieces):

  while True:
    for i in range(4):
      if pieces[i] > pieces[i + 1]:
        pieces = swap_pieces(i, i + 1, pieces)
        # pieces는 int를 담고 있는 리스트여서 map(str,pieces)를 통해서
        # str를 담고 있는 리스트로 변환
        print(str(' '.join(map(str, pieces))))

    if pieces == sorted(pieces):
      return
    else:
      continue


def swap_pieces(i, j, pieces):
  tmp = pieces[i]
  pieces[i] = pieces[j]
  pieces[j] = tmp

  return pieces


pieces = list(map(int, stdin.readline().split()))
ans(pieces)
