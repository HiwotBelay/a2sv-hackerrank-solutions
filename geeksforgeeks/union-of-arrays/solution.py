def findUnion(a, b):
    # Use set to get distinct elements from both arrays
    union_set = set(a) | set(b)
    # Convert back to list and return
    return list(union_set)

# Example usage (for testing)
if __name__ == '__main__':
    # Example 1
    a1 = [1, 2, 3, 2, 1]
    b1 = [3, 2, 2, 3, 3, 2]
    result1 = findUnion(a1, b1)
    print(sorted(result1))  # [1, 2, 3]
    
    # Example 2
    a2 = [1, 2, 3]
    b2 = [4, 5, 6]
    result2 = findUnion(a2, b2)
    print(sorted(result2))  # [1, 2, 3, 4, 5, 6]
    
    # Example 3
    a3 = [1, 2, 1, 1, 2]
    b3 = [2, 2, 1, 2, 1]
    result3 = findUnion(a3, b3)
    print(sorted(result3))  # [1, 2]
