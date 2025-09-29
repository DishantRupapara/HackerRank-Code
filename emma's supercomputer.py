def get_plus_cells(r, c, k):
    """Return set of cells occupied by plus centered at (r,c) with arm length k"""
    cells = set()
    cells.add((r,c))
    for d in range(1, k+1):
        cells.add((r+d, c))
        cells.add((r-d, c))
        cells.add((r, c+d))
        cells.add((r, c-d))
    return cells

def twoPluses(grid):
    n = len(grid)
    m = len(grid[0])
    pluses = []

    # Compute maximum arm length for each cell
    max_arm = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'G':
                k = 0
                while True:
                    if i-k < 0 or i+k >= n or j-k < 0 or j+k >= m:
                        break
                    if grid[i-k][j] != 'G' or grid[i+k][j] != 'G' or grid[i][j-k] != 'G' or grid[i][j+k] != 'G':
                        break
                    pluses.append((i,j,k, 1 + 4*k, get_plus_cells(i,j,k)))
                    k += 1

    # Sort pluses by area descending
    pluses.sort(key=lambda x: -x[3])
    
    max_product = 0
    for i in range(len(pluses)):
        for j in range(i+1, len(pluses)):
            cells1 = pluses[i][4]
            cells2 = pluses[j][4]
            if cells1.isdisjoint(cells2):
                product = pluses[i][3] * pluses[j][3]
                if product > max_product:
                    max_product = product
    return max_product

# Input
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
print(twoPluses(grid))
