def absolutePermutation(n, k):
    if k == 0:
        return list(range(1, n+1))
    if n % (2*k) != 0:
        return [-1]
    
    perm = []
    add = True  # toggle to add or subtract k
    for i in range(1, n+1):
        if add:
            perm.append(i + k)
        else:
            perm.append(i - k)
        # toggle every k elements
        if i % k == 0:
            add = not add
    return perm

# Input
q = int(input())  # number of queries
for _ in range(q):
    n, k = map(int, input().split())
    result = absolutePermutation(n, k)
    print(*result)
