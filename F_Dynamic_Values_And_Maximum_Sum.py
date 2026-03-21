import sys
import heapq
from collections import defaultdict


def better(a_dist, a_leaf, b_dist, b_leaf):
    if a_dist != b_dist:
        return a_dist > b_dist
    return a_leaf < b_leaf


class TopK:
    def __init__(self, k):
        self.k = k
        self.small = []  # min-heap: current top-k elements
        self.large = []  # max-heap via negatives: the rest
        self.small_cnt = defaultdict(int)
        self.del_small = defaultdict(int)
        self.del_large = defaultdict(int)
        self.small_size = 0
        self.large_size = 0
        self.small_sum = 0

    def _prune_small(self):
        while self.small and self.del_small[self.small[0]] > 0:
            x = heapq.heappop(self.small)
            self.del_small[x] -= 1

    def _prune_large(self):
        while self.large and self.del_large[-self.large[0]] > 0:
            x = -heapq.heappop(self.large)
            self.del_large[x] -= 1

    def _add_small(self, x):
        heapq.heappush(self.small, x)
        self.small_cnt[x] += 1
        self.small_size += 1
        self.small_sum += x

    def _add_large(self, x):
        heapq.heappush(self.large, -x)
        self.large_size += 1

    def _extract_small(self):
        self._prune_small()
        x = heapq.heappop(self.small)
        self.small_size -= 1
        self.small_sum -= x
        self.small_cnt[x] -= 1
        return x

    def _extract_large(self):
        self._prune_large()
        x = -heapq.heappop(self.large)
        self.large_size -= 1
        return x

    def _rebalance(self):
        if self.k == 0:
            return

        self._prune_small()
        self._prune_large()

        while self.small_size < self.k and self.large_size > 0:
            x = self._extract_large()
            self._add_small(x)

        while self.small_size > self.k:
            x = self._extract_small()
            self._add_large(x)

        self._prune_small()
        self._prune_large()

        while self.small_size > 0 and self.large_size > 0:
            self._prune_small()
            self._prune_large()
            if self.small_size == 0 or self.large_size == 0:
                break
            lo_top = self.small[0]
            hi_top = -self.large[0]
            if hi_top <= lo_top:
                break
            a = self._extract_large()
            b = self._extract_small()
            self._add_small(a)
            self._add_large(b)

    def insert(self, x):
        if self.k == 0:
            self._add_large(x)
            return

        self._prune_small()
        if self.small_size < self.k:
            self._add_small(x)
        else:
            self._prune_small()
            if self.small and x > self.small[0]:
                y = self._extract_small()
                self._add_large(y)
                self._add_small(x)
            else:
                self._add_large(x)
        self._rebalance()

    def erase(self, x):
        if self.k > 0 and self.small_cnt[x] > 0:
            self.small_cnt[x] -= 1
            self.del_small[x] += 1
            self.small_size -= 1
            self.small_sum -= x
        else:
            self.del_large[x] += 1
            self.large_size -= 1
        self._rebalance()

    def update(self, old_val, new_val):
        self.erase(old_val)
        self.insert(new_val)

    def get_sum(self):
        return self.small_sum


def solve():
    input = sys.stdin.readline
    t = int(input())
    out = []

    for _ in range(t):
        n, k = map(int, input().split())
        a = [0] + list(map(int, input().split()))

        if n == 1:
            out.append(str(a[1]))
            continue

        m = n - 1
        to = [0] * (2 * m)
        rev = [0] * (2 * m)
        adj = [[] for _ in range(n + 1)]

        eidx = 0
        for _e in range(m):
            u, v = map(int, input().split())
            d1 = eidx
            d2 = eidx + 1
            eidx += 2
            to[d1] = v
            to[d2] = u
            rev[d1] = d2
            rev[d2] = d1
            adj[u].append(d1)
            adj[v].append(d2)

        deg = [0] * (n + 1)
        leaves = []
        for i in range(1, n + 1):
            deg[i] = len(adj[i])
            if deg[i] == 1:
                leaves.append(i)

        leaf_id = {}
        for i, v in enumerate(leaves):
            leaf_id[v] = i
        L = len(leaves)

        # Root tree at 1 for traversal order.
        parent = [0] * (n + 1)
        parent_in_edge = [-1] * (n + 1)  # directed edge parent->u
        parent_out_edge = [-1] * (n + 1)  # directed edge u->parent
        order = []
        st = [1]
        parent[1] = -1

        while st:
            u = st.pop()
            order.append(u)
            for d in adj[u]:
                v = to[d]
                if v == parent[u]:
                    continue
                parent[v] = u
                parent_in_edge[v] = d
                parent_out_edge[v] = rev[d]
                st.append(v)

        # msg[d] = g(u, v): at node u (where d is u->v), best leaf in component
        # reachable from u without going to v, as pair (dist, leaf).
        msg_dist = [0] * (2 * m)
        msg_leaf = [0] * (2 * m)

        # Postorder: compute child->parent messages.
        for u in reversed(order):
            if u == 1:
                continue
            p = parent[u]
            best_d = -1
            best_l = 10**18
            for d in adj[u]:
                v = to[d]
                if v == p:
                    continue
                rd = rev[d]  # v->u
                cand_d = msg_dist[rd] + 1
                cand_l = msg_leaf[rd]
                if best_l == 10**18 or better(cand_d, cand_l, best_d, best_l):
                    best_d = cand_d
                    best_l = cand_l
            if best_l == 10**18:
                best_d = 0
                best_l = u
            d_up = parent_out_edge[u]  # u->p
            msg_dist[d_up] = best_d
            msg_leaf[d_up] = best_l

        # Preorder: compute parent->child messages.
        for u in order:
            # Build best two candidates among all neighbors.
            best1_edge = -1
            best1_d = -1
            best1_l = 10**18
            best2_edge = -1
            best2_d = -1
            best2_l = 10**18

            for d in adj[u]:
                rd = rev[d]  # neighbor->u
                cand_d = msg_dist[rd] + 1
                cand_l = msg_leaf[rd]
                if best1_edge == -1 or better(cand_d, cand_l, best1_d, best1_l):
                    best2_edge, best2_d, best2_l = best1_edge, best1_d, best1_l
                    best1_edge, best1_d, best1_l = d, cand_d, cand_l
                elif best2_edge == -1 or better(cand_d, cand_l, best2_d, best2_l):
                    best2_edge, best2_d, best2_l = d, cand_d, cand_l

            for d in adj[u]:
                v = to[d]
                if v == parent[u]:
                    continue
                # Need g(u, v): best among neighbors except v.
                if best1_edge == d:
                    use_edge = best2_edge
                    use_d = best2_d
                    use_l = best2_l
                else:
                    use_edge = best1_edge
                    use_d = best1_d
                    use_l = best1_l

                out_d = d  # u->v
                if use_edge == -1:
                    msg_dist[out_d] = 0
                    msg_leaf[out_d] = u
                else:
                    msg_dist[out_d] = use_d
                    msg_leaf[out_d] = use_l

        # For each node, best 2 outgoing edges by candidate (for destination choice).
        best1 = [-1] * (n + 1)
        best2 = [-1] * (n + 1)
        best1_d = [-1] * (n + 1)
        best2_d = [-1] * (n + 1)
        best1_l = [10**18] * (n + 1)
        best2_l = [10**18] * (n + 1)

        for u in range(1, n + 1):
            for d in adj[u]:
                rd = rev[d]
                cand_d = msg_dist[rd] + 1
                cand_l = msg_leaf[rd]
                if best1[u] == -1 or better(cand_d, cand_l, best1_d[u], best1_l[u]):
                    best2[u], best2_d[u], best2_l[u] = best1[u], best1_d[u], best1_l[u]
                    best1[u], best1_d[u], best1_l[u] = d, cand_d, cand_l
                elif best2[u] == -1 or better(cand_d, cand_l, best2_d[u], best2_l[u]):
                    best2[u], best2_d[u], best2_l[u] = d, cand_d, cand_l

        # next_state for directed edge state d (state at node to[d], parent is rev[d]).
        next_state = [-1] * (2 * m)
        for d in range(2 * m):
            u = to[d]  # current node
            excluded = rev[d]  # u->parent
            if best1[u] == -1:
                next_state[d] = -1
            elif best1[u] != excluded:
                next_state[d] = best1[u]
            else:
                next_state[d] = best2[u]

        # terminal leaf for each directed-edge state.
        term = [0] * (2 * m)
        for d0 in range(2 * m):
            if term[d0] != 0:
                continue
            path = []
            cur = d0
            while True:
                if term[cur] != 0:
                    leaf = term[cur]
                    break
                path.append(cur)
                nx = next_state[cur]
                if nx == -1:
                    leaf = to[cur]
                    break
                cur = nx
            for d in path:
                term[d] = leaf

        # Initial root = 1, contributions from all u != 1.
        leaf_sum = [0] * L
        for u in range(2, n + 1):
            d_in = parent_in_edge[u]  # parent->u
            lf = term[d_in]
            leaf_sum[leaf_id[lf]] += a[u]

        m_nonleaf = min(k - 1, L)
        m_leaf = min(k - 1, max(0, L - 1))

        top_nonleaf = TopK(m_nonleaf)
        if m_leaf == m_nonleaf:
            top_leaf = top_nonleaf
        else:
            top_leaf = TopK(m_leaf)

        for v in leaf_sum:
            top_nonleaf.insert(v)
            if top_leaf is not top_nonleaf:
                top_leaf.insert(v)

        def update_leaf(idx, delta):
            old = leaf_sum[idx]
            new = old + delta
            top_nonleaf.update(old, new)
            if top_leaf is not top_nonleaf:
                top_leaf.update(old, new)
            leaf_sum[idx] = new

        ans = 0

        def eval_root(r):
            if deg[r] == 1:
                return a[r] + top_leaf.get_sum()
            return a[r] + top_nonleaf.get_sum()

        ans = max(ans, eval_root(1))

        # Reroot DFS over roots.
        sys.setrecursionlimit(1_000_000)

        def dfs_root(r, p):
            nonlocal ans
            for d in adj[r]:
                x = to[d]
                if x == p:
                    continue

                # Move root r -> x.
                old_lf = term[d]       # x was non-root with parent r
                new_lf = term[rev[d]]  # r becomes non-root with parent x

                update_leaf(leaf_id[old_lf], -a[x])
                update_leaf(leaf_id[new_lf], +a[r])

                ans = max(ans, eval_root(x))
                dfs_root(x, r)

                # Rollback.
                update_leaf(leaf_id[new_lf], -a[r])
                update_leaf(leaf_id[old_lf], +a[x])

        dfs_root(1, 0)

        out.append(str(ans))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
