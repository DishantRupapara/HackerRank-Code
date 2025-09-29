from collections import Counter

def happyLadybugs(b):
    counts = Counter(b)
    
    for k, v in counts.items():
        if k != '_' and v == 1:
            return "NO"
    
    if '_' in counts:
        return "YES"
    
    n = len(b)
    for i in range(n):
        if (i > 0 and b[i] == b[i-1]) or (i < n-1 and b[i] == b[i+1]):
            continue
        return "NO"
    
    return "YES"

g = int(input())
for _ in range(g):
    n = int(input())
    b = input().strip()
    print(happyLadybugs(b))
