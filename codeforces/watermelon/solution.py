w = int(input())

# Check if we can divide into two even parts
# Both parts must be positive and even
# If w is odd, impossible (odd = even + odd)
# If w is 2, impossible (would need 2+0 or 0+2, but 0 is not positive)
# If w >= 4 and even, possible (e.g., 2 + (w-2))

if w >= 4 and w % 2 == 0:
    print("YES")
else:
    print("NO")
