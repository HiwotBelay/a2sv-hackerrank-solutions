t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    
    # Check if one number is sum of other two
    if a == b + c or b == a + c or c == a + b:
        print("YES")
    else:
        print("NO")
