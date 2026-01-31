def swap_case(s):
    result = ""
    for char in s:
        # If character is lowercase, convert to uppercase
        if char.islower():
            result += char.upper()
        # If character is uppercase, convert to lowercase
        elif char.isupper():
            result += char.lower()
        # If it's not a letter (like space, number, punctuation), keep it as is
        else:
            result += char
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
