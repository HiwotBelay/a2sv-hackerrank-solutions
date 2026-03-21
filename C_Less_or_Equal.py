import sys


def solve() -> None:
    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))

    if k == 0:
        # Need 0 elements <= x, so choose x < a[0], but x must be >= 1
        if a[0] == 1:
            print(-1)
        else:
            print(1)
        return

    x = a[k - 1]
    if k < n and a[k] == x:
        print(-1)
    else:
        print(x)


if __name__ == "__main__":
    solve()
n,k = map(int, input().split())
arr=list(map(int, input().split()))

arr.sort()

if k==0:
    if arr[0]==1:
        print(-1)
    else:
        print(arr[0]-1)
else:
    if k<n and arr[k]==arr[k-1]:
        print(-1)
    else:
        if k<n:
            print(arr[k]-1)
        else:
            print(arr[k-1])