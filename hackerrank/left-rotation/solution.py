def rotateLeft(d, arr):
    # Rotate array d positions to the left
    # Elements that fall off left reappear at right (circular rotation)
    n = len(arr)
    # Use slicing: take from index d to end, then from start to d
    return arr[d:] + arr[:d]

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = rotateLeft(d, arr)
    print(' '.join(map(str, result)))
