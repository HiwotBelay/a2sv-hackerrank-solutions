def isSubset(a, b):
    # Count how many times each element appears in a
    count_a = {}
    for num in a:
        count_a[num] = count_a.get(num, 0) + 1
    
    # Check if all elements in b exist in a with enough count
    for num in b:
        if num not in count_a or count_a[num] == 0:
            return False
        count_a[num] -= 1
    
    return True

# Example usage
if __name__ == '__main__':
    # Test case 1
    a1 = [11, 7, 1, 13, 21, 3, 7, 3]
    b1 = [11, 3, 7, 1, 7]
    print(isSubset(a1, b1))  # True
    
    # Test case 2
    a2 = [1, 2, 3, 4, 4, 5, 6]
    b2 = [1, 2, 4]
    print(isSubset(a2, b2))  # True
    
    # Test case 3
    a3 = [10, 5, 2, 23, 19]
    b3 = [19, 5, 3]
    print(isSubset(a3, b3))  # False
