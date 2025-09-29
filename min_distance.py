def minimumDistances(a):
    min_dist = float('inf')  # start with very large number
    n = len(a)
    
    for i in range(n):
        for j in range(i+1, n):  # start from i+1 to avoid i==j
            if a[i] == a[j]:
                min_dist = min(min_dist, j - i)
    
    return min_dist if min_dist != float('inf') else -1

# Input
n = int(input())
a = list(map(int, input().split()))
print(minimumDistances(a))
