def split_and_join(line):
    # Split the string on spaces
    words = line.split(" ")
    
    # Join the words with hyphen
    result = "-".join(words)
    
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
