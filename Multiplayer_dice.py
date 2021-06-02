import random as rand

n = int(input("Number of Players: ")) #players
m = int(input("Number of Rounds: ")) #rounds

for i in range(m):
    print(f"== Round {i+1} ==")
    for a in range(n):
        print(f"P{a+1}: {rand.randint(1, 6)}")
