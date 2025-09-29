def kaprekarNumbers(p, q):
    results = []
    for n in range(p, q + 1):
        d = len(str(n))        # number of digits in n
        sq = str(n * n)        # square as string
        
        # split into left and right
        right = int(sq[-d:]) if d <= len(sq) else int(sq)
        left = int(sq[:-d]) if sq[:-d] else 0
        
        if left + right == n:
            results.append(n)
    
    if results:
        print(" ".join(map(str, results)))
    else:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())
    kaprekarNumbers(p, q)
