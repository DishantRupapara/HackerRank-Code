def flatlandSpaceStations(n, c):
    c.sort()   # sort the stations
    max_dist = 0

    # Distance before first station
    max_dist = max(max_dist, c[0] - 0)

    # Distances between stations
    for i in range(len(c) - 1):
        gap = c[i+1] - c[i]
        max_dist = max(max_dist, gap // 2)

    # Distance after last station
    max_dist = max(max_dist, n - 1 - c[-1])

    return max_dist

# Input
n, m = map(int, input().split())
c = list(map(int, input().split()))
print(flatlandSpaceStations(n, c))
