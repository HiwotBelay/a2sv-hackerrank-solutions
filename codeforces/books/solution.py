import sys

input = sys.stdin.readline

n, t = map(int, input().split())
a = list(map(int, input().split()))

# Use sliding window to find the longest contiguous subarray with sum <= t
# Since Valera can start from any book and read sequentially, we need to find
# the longest contiguous subarray where the sum of reading times <= t

left = 0
current_sum = 0
max_books = 0

for right in range(n):
    # Add the current book to the window
    current_sum += a[right]
    
    # Shrink the window from left if sum exceeds t
    while current_sum > t and left <= right:
        current_sum -= a[left]
        left += 1
    
    # Update maximum number of books
    max_books = max(max_books, right - left + 1)

print(max_books)
