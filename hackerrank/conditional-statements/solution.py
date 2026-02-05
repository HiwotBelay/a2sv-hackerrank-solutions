if __name__ == '__main__':
    n = int(input().strip())
    
    # If n is odd, print Weird
    if n % 2 == 1:
        print("Weird")
    # If n is even
    else:
        # If n is in range 2 to 5, print Not Weird
        if 2 <= n <= 5:
            print("Not Weird")
        # If n is in range 6 to 20, print Weird
        elif 6 <= n <= 20:
            print("Weird")
        # If n is greater than 20, print Not Weird
        else:
            print("Not Weird")
