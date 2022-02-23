import sys
import random


def get_next_player(player_list: list) -> str:
    return random.choice(player_list)


def is_match_valid(sender: str, receiver: str) -> bool:
    if sender.lower() == receiver.lower():
        return False
    for tup in allowed_mappings:
        if tup == (sender, receiver) or tup[::-1] == (sender, receiver):
            return True
    for tup in restricted_mappings:
        if tup == (sender, receiver) or tup[::-1] == (sender, receiver):
            return False
    return True


def solve_for_matching(santa_player_list: list, receiver_player_list: list) -> bool:
    if len(santa_player_list) == 0:
        return True
    next_player = get_next_player(santa_player_list)
    for receiver in receiver_player_list:
        if is_match_valid(next_player, receiver):   
            answer.append((next_player, receiver))
            receiver_player_list.remove(receiver)
            santa_player_list.remove(next_player)
            if solve_for_matching(santa_player_list, receiver_player_list):
                return True
            answer.remove((next_player, receiver))
            receiver_player_list.append(receiver)
            santa_player_list.append(next_player)
    return False



if __name__ == '__main__':
    print("Welcome to Secret Santa Using Backtracking !")

    players = ['A', 'B', 'C']
    receiver_list = players.copy()
    allowed_mappings = [()]
    restricted_mappings = [('B', 'C')]
    answer = list()

    if not players:
        print("SNAP ! Need Players :(")
        sys.exit(0)

    result = solve_for_matching(players, receiver_list)

    if result:
        print(f"Generated Pairs :: {answer}")
    else:
        print(f"No Pairing Possible :: {answer}")