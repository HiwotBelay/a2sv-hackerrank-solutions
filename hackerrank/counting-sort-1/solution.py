import sys


def solve() -> None:
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))

    freq = [0] * 100
    for v in arr:
        if 0 <= v < 100:
            freq[v] += 1

    print(" ".join(map(str, freq)))


if __name__ == "__main__":
    solve()
