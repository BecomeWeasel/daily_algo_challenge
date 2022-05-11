def solution(k, room_number):
    answer = []

    # 다음에 배정할 방의 번호들
    next_room = dict()

    FREE = 0

    for request in room_number:
        # request 방이 빈방이라면 number에 FREE
        number = next_room.get(request, FREE)

        # next_room에 번호가 적혀있다면 거기서부터 탐색 시작
        # 원하는 방은 이미 차있으니 number 부터 탐색해보세요
        if number:
            # 처음 들렸던 방을 기록
            visit = [request]
            # 빈방 체크
            while True:
                candidate_room = number
                number = next_room.get(number, FREE)

                # 새로 안내받은 방이 FREE라면 그방으로 가면됨
                if number == FREE:
                    answer.append(candidate_room)
                    # 다음에 candidate_room으로 접근을한다면
                    # candidate_room+1 방으로 가라고 알려줌
                    next_room[candidate_room] = candidate_room + 1

                    # 탐색을 빠르게 하기위해서
                    # 이전에 지나쳐왔던 방들한테도 candidate_room+1 방으로 알려줌
                    # 이 코드가 없으면 다시 처음부터 빈방들에 대해서 물어보면서 가야함
                    # -> TLE
                    for i in visit:
                        next_room[i] = candidate_room + 1
                    break
                visit.append(number)
        # 처음부터 빈방이라면 FREE
        # 원하는 방인 request 방에 넣어줄수 있음
        elif number == FREE:
            answer.append(request)
            next_room[request] = request + 1

    return answer


if __name__ == "__main__":
    print(solution(10, [1, 3, 4, 1, 3, 1]))
