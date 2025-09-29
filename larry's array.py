def count_inversions(arr):
    # Helper function to merge two halves and count inversions
    def merge_count(left, right):
        merged = []
        inv_count = 0
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv_count += len(left) - i
                j += 1
        merged += left[i:]
        merged += right[j:]
        return merged, inv_count

    # Recursive merge sort to count inversions
    def sort_count(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, inv_left = sort_count(arr[:mid])
        right, inv_right = sort_count(arr[mid:])
        merged, inv_merge = merge_count(left, right)
        return merged, inv_left + inv_right + inv_merge

    _, total_inversions = sort_count(arr)
    return total_inversions

def larrysArray(A):
    inv_count = count_inversions(A)
    return "YES" if inv_count % 2 == 0 else "NO"

# Input handling
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    print(larrysArray(A))
