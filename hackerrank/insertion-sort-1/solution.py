import sys


def solve() -> None:
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))

    x = arr[-1]
    i = n - 2

    while i >= 0 and arr[i] > x:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1

    arr[i + 1] = x
    print(*arr)


if __name__ == "__main__":
    solve()
