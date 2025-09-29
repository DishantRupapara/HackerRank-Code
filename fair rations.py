def fairRations(B):
    loaves = 0
    n = len(B)
    
    for i in range(n - 1):
        if B[i] % 2 != 0:      # if current person has odd loaves
            B[i] += 1           # give 1 to current
            B[i+1] += 1         # give 1 to next
            loaves += 2         # count 2 loaves given
    
    # check if the last person is even
    if B[-1] % 2 != 0:
        return "NO"
    else:
        return str(loaves)

# Input
n = int(input())
B = list(map(int, input().split()))
print(fairRations(B))
