n = int(input())

# Create phone book dictionary
phone_book = {}

# Read n entries
for _ in range(n):
    entry = input().split()
    name = entry[0]
    phone = entry[1]
    phone_book[name] = phone

# Read queries until EOF
while True:
    try:
        query = input().strip()
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
    except EOFError:
        break
