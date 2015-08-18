from random import randint
from time import sleep

cpu_score = 0
player_score = 0

while cpu_score < 10 and player_score < 10:
    # 0 is heads, 1 is tails

    possibilities = {0: "heads", 1: "tails"}

    toss1 = randint(0, 1)
    print "TOSS:", possibilities[toss1]
    sleep(1)
    toss2 = randint(0, 1)
    print "TOSS:", possibilities[toss2]
    sleep(1)

    if toss1 == 1 and toss2 == 1:
        cpu_score = cpu_score + 1
    elif toss1 == 0 and toss2 == 0:
        player_score = player_score + 1
    else:
        sleep(1)
        print "OOPS NO POINTS"

    print "CPU:", cpu_score
    sleep(1)
    print "YOU:", player_score
    sleep(1)

    answer = raw_input("PLAY AGAIN?")
    if answer == "no" or answer == "n":
        print "TOO BAD!"
