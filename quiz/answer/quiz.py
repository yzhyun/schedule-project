
def solution(players, callings):
    answer = []
    dict_players = {}
    dict_rank = {}
    for i , val in enumerate (players):
        dict_players[i] = val
        dict_rank[val] = i
    for name in callings:
        print(name)
        print(dict_rank[name])
        dict_rank[dict_players[dict_rank[name]-1]] += 1
        dict_players[dict_rank[dict_players[dict_rank[name] - 1]]] = dict_players[dict_rank[name] - 1]
        dict_rank[name] -= 1

        dict_players[dict_rank[name]] = name

    answer = list(dict_players.values())

    return answer

players = ["mumu", "soe", "poe","kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

print(solution(players, callings))