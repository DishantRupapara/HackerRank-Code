def detonate(grid):
    R = len(grid)
    C = len(grid[0])
    new_grid = [['O']*C for _ in range(R)]
    
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'O':
                new_grid[i][j] = '.'
                if i > 0:
                    new_grid[i-1][j] = '.'
                if i < R-1:
                    new_grid[i+1][j] = '.'
                if j > 0:
                    new_grid[i][j-1] = '.'
                if j < C-1:
                    new_grid[i][j+1] = '.'
    return [''.join(row) for row in new_grid]

def bomberMan(n, grid):
    if n == 1:
        return grid
    if n % 2 == 0:
        return ['O'*len(grid[0]) for _ in grid]
    
    # First detonation pattern (t=3)
    pattern1 = detonate(grid)
    if n % 4 == 3:
        return pattern1
    # Second detonation pattern (t=5)
    pattern2 = detonate(pattern1)
    return pattern2

# Input
r, c, n = map(int, input().split())
grid = [input().strip() for _ in range(r)]
result = bomberMan(n, grid)
print('\n'.join(result))
