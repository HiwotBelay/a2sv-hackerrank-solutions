import sys


def solve() -> None:
    input = sys.stdin.readline
    t = int(input())
    out = []

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        # Build logs for O(1) RMQ queries with sparse table.
        logs = [0] * (n + 1)
        for i in range(2, n + 1):
            logs[i] = logs[i // 2] + 1

        k = logs[n] + 1
        st = [a[:]]

        j = 1
        while (1 << j) <= n:
            prev = st[j - 1]
            size = n - (1 << j) + 1
            row = [0] * size
            half = 1 << (j - 1)
            for i in range(size):
                left = prev[i]
                right = prev[i + half]
                row[i] = left if left < right else right
            st.append(row)
            j += 1

        q = int(input())
        for _ in range(q):
            l, r = map(int, input().split())
            length = r - l + 1
            p = logs[length]
            x = st[p][l]
            y = st[p][r - (1 << p) + 1]
            out.append(str(x if x < y else y))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
