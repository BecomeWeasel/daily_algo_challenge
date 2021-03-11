from sys import stdin

N, L = map(int, stdin.readline().split())


def ans():
  traffic_light_infos = list()

  for i in range(N):
    traffic_light_infos.append(list(map(int, stdin.readline().split())))

  clock = 0
  distance = 0

  for traffic_light in traffic_light_infos:
    # 다음 신호등까지 이동
    if distance < traffic_light[0]:
      clock += traffic_light[0] - distance
      distance += traffic_light[0] - distance

    # 도착했을때의 시간을 기준으로 R+G가 반복되고 남은 나머지가
    # R보다 작다면 그 시간에 여전히 R이기 때문에 그자리에서
    # R-나머지 시간만큼 기다려야함.
    if (clock % (traffic_light[1] + traffic_light[2])) < traffic_light[1]:
      clock += traffic_light[1] - clock % (traffic_light[1] + traffic_light[2])
    else:
      continue

  # 모든 신호등을 지났는데 여전히 거리가 남아있을 경우 1초에 1미터씩 전진
  if distance <= L:
    clock += L - distance

  return (clock)



print(ans())