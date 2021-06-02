import random as rand

n = int(input("Number of Players: ")) #players
m = int(input("Number of Rounds: ")) #rounds
player_scores = {}

for i in range(n):
    player_scores[i+1] = []

for i in range(m):
    print(f"== Round {i+1} ==")

    for a in range(n):
        score = rand.randint(1, 6)
        print(f"P{a+1}: {score}")
        player_scores[(a+1)].append(score)        

print(player_scores)
