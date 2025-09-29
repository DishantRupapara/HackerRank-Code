def howManyGames(p, d, m, s):
    count = 0
    while s >= p:
        s -= p
        count += 1
        p = max(p - d, m)   # price cannot go below m
    return count

# Input
p, d, m, s = map(int, input().split())
print(howManyGames(p, d, m, s))
