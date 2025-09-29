def surfaceArea(A):
    H = len(A)
    W = len(A[0])
    area = 0
    
    for i in range(H):
        for j in range(W):
            # top and bottom
            area += 2
            
            # up
            if i == 0:
                area += A[i][j]
            else:
                area += max(A[i][j] - A[i-1][j], 0)
            
            # down
            if i == H-1:
                area += A[i][j]
            else:
                area += max(A[i][j] - A[i+1][j], 0)
            
            # left
            if j == 0:
                area += A[i][j]
            else:
                area += max(A[i][j] - A[i][j-1], 0)
            
            # right
            if j == W-1:
                area += A[i][j]
            else:
                area += max(A[i][j] - A[i][j+1], 0)
    
    return area

# Input
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

print(surfaceArea(A))
