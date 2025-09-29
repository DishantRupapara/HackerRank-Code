def chocolateFeast(n, c, m):
    chocolates = n // c         # buy chocolates with money
    wrappers = chocolates       # initial wrappers
    while wrappers >= m:
        free = wrappers // m    # trade wrappers for free chocolates
        chocolates += free
        wrappers = wrappers - free * m + free  # update wrappers
    return chocolates

# Input
t = int(input())  # number of test cases
for _ in range(t):
    n, c, m = map(int, input().split())
    print(chocolateFeast(n, c, m))
