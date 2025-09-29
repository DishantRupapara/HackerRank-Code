def stones(n, a, b):
    last_stones = set()
    for i in range(n):
        value = i * a + (n - 1 - i) * b
        last_stones.add(value)
    return sorted(last_stones)

# Input
t = int(input())  # number of test cases
for _ in range(t):
    n = int(input())
    a = int(input())
    b = int(input())
    result = stones(n, a, b)
    print(*result)
