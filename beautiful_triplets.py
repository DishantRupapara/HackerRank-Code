def beautifulTriplets(d, arr):
    count = 0
    arr_set = set(arr)  # for fast lookup
    
    for num in arr:
        if (num + d in arr_set) and (num + 2*d in arr_set):
            count += 1
    return count


if __name__ == '__main__':
    n, d = map(int, input().split())      # first line: n and d
    arr = list(map(int, input().split())) # second line: array
    
    result = beautifulTriplets(d, arr)
    print(result)
