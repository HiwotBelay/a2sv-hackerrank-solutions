import sys


def solve() -> None:
    input = sys.stdin.readline
    t = int(input())
    out = []

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        # Precompute floor(log2(x)) for x in [1..n]
        logs = [0] * (n + 1)
        for i in range(2, n + 1):
            logs[i] = logs[i // 2] + 1

        # Sparse table: st[p][i] = min on segment [i, i + 2^p - 1]
        st = [a]
        p = 1
        while (1 << p) <= n:
            prev = st[p - 1]
            step = 1 << (p - 1)
            size = n - (1 << p) + 1
            row = [0] * size
            for i in range(size):
                left = prev[i]
                right = prev[i + step]
                row[i] = left if left < right else right
            st.append(row)
            p += 1

        q = int(input())
        for _ in range(q):
            l, r = map(int, input().split())
            length = r - l + 1
            p = logs[length]
            left_min = st[p][l]
            right_min = st[p][r - (1 << p) + 1]
            out.append(str(left_min if left_min < right_min else right_min))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
