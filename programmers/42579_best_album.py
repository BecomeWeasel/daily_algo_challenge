from collections import defaultdict

play_per_genre = defaultdict(int)


class music:
    def __init__(self, genre, playtime, number, plays):
        self.genre = genre
        self.playtime = playtime
        self.number = number
        self.plays = plays

    # class를 만들어서 비교함수 만들기
    def __lt__(self, value):
        if play_per_genre[self.genre] > play_per_genre[value.genre]:
            return True
        elif play_per_genre[self.genre] == play_per_genre[value.genre]:
            if self.plays[self.number] > self.plays[value.number]:
                return True
            elif self.plays[self.number] == self.plays[value.number]:
                if self.number < value.number:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        return super().__lt__(value)


def solution(genres, plays):
    answer = []

    for i, play in enumerate(plays):
        play_per_genre[genres[i]] += play

    songs = [x for x in range(len(plays))]

    songs.sort(key=lambda x: (-play_per_genre[genres[x]], -plays[x], x))

    # musics=[music(genres[x],plays[x],x,plays) for x in range(len(plays))]
    # 문제의 기준대로
    # 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
    # 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
    # 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
    # 정렬한후
    # musics.sort()

    genre_in_album = defaultdict(int)

    # 각 장르별 수록곡의 회수를 더해줌
    for song in songs:
        if genre_in_album[genres[song]] == 2:
            continue
        else:
            answer.append(song)
            genre_in_album[genres[song]] += 1

    return answer
