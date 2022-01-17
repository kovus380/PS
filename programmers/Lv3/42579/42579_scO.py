from collections import defaultdict


def solution(genres, plays):
    answer = []
    genre_play = defaultdict(list)
    genre_play_sum = defaultdict(int)

    for idx, genre in enumerate(genres):
        genre_play[genre].append([idx, plays[idx]])
        genre_play_sum[genre] += plays[idx]

    sorted_genre_play_sum = sorted(genre_play_sum.items(), key = lambda x: x[1], reverse=True)
    for genre in genre_play:
        genre_play[genre] = sorted(genre_play[genre], key = lambda x: x[1], reverse=True)

    for genre in sorted_genre_play_sum:
        answer.append(genre_play[genre[0]][0][0])
        if len(genre_play[genre[0]]) >= 2:
            answer.append(genre_play[genre[0]][1][0])

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
res = solution(genres, plays)
print(res)