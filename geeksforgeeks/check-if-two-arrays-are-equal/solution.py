def check(a, b):
    # just sort both and check if they're same
    return sorted(a) == sorted(b)

# Example usage
if __name__ == '__main__':
    # Test case 1
    a1 = [1, 2, 5, 4, 0]
    b1 = [2, 4, 5, 0, 1]
    print(check(a1, b1))  # True
    
    # Test case 2
    a2 = [1, 2, 5]
    b2 = [2, 4, 15]
    print(check(a2, b2))  # False
