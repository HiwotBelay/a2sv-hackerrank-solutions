k, n, w = map(int, input().split())

# Total cost = k + 2k + 3k + ... + wk = k * (1 + 2 + ... + w) = k * w * (w + 1) / 2
total_cost = k * w * (w + 1) // 2

# Calculate how much he needs to borrow
borrow = max(0, total_cost - n)

print(borrow)
