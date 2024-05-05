import random
import time

# moves
R = "Rock"
P = "Paper"
S = "Scissors"

moves = [R, P, S]

scoreboard = {"you": 0, "com": 0}


def gameplay(x):
    # passed to template and append to image name to prevent browser caching
    time_now = time.time()

    player_move = x
    comp_move = random.choice(moves)

    if player_move == R:
        if comp_move == R:
            decision = "Draw"
        elif comp_move == P:
            decision = "Com Wins!"
            scoreboard["com"] += 1
        else:
            decision = "You win!"
            scoreboard["you"] += 1

    elif player_move == P:
        if comp_move == P:
            decision = "Draw"
        elif comp_move == S:
            decision = "Com Wins!"
            scoreboard["com"] += 1
        else:
            decision = "You win!"
            scoreboard["you"] += 1

    else:
        if comp_move == S:
            decision = "Draw"
        elif comp_move == R:
            decision = "Com Wins!"
            scoreboard["com"] += 1
        else:
            decision = "You win!"
            scoreboard["you"] += 1
    return (comp_move, decision, time_now, scoreboard)
