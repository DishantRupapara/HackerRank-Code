def gridSearch(G, P):
    R = len(G)
    C = len(G[0])
    r = len(P)
    c = len(P[0])
    
    for i in range(R - r + 1):
        for j in range(C - c + 1):
            match = True
            for x in range(r):
                if G[i + x][j:j+c] != P[x]:
                    match = False
                    break
            if match:
                return "YES"
    return "NO"

# Input
t = int(input())  # number of test cases

for _ in range(t):
    R, C = map(int, input().split())
    G = [input().strip() for _ in range(R)]
    r, c = map(int, input().split())
    P = [input().strip() for _ in range(r)]
    print(gridSearch(G, P))
