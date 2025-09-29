def serviceLane(n, t, width, cases):
    results = []
    for case in cases:
        i, j = case
        results.append(min(width[i:j+1]))  # min width in the range
    return results

# Input
n, t = map(int, input().split())
width = list(map(int, input().split()))
cases = [list(map(int, input().split())) for _ in range(t)]

# Output
for result in serviceLane(n, t, width, cases):
    print(result)
