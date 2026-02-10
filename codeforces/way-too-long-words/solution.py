n = int(input())

for _ in range(n):
    word = input()
    
    if len(word) > 10:
        # Abbreviate: first letter + (length-2) + last letter
        abbrev = word[0] + str(len(word) - 2) + word[-1]
        print(abbrev)
    else:
        print(word)
