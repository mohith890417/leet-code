
class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)

        vals = sorted(set(nums))
        m = len(vals)

        def update(bit, i, v):
            while i <= m:
                bit[i] += v
                i += i & -i

        def query(bit, i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        def kth(bit, target):
            idx = 0
            step = 1 << (m.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= m and bit[nxt] < target:
                    idx = nxt
                    target -= bit[nxt]
                step >>= 1

            return idx + 1

        count = [0] * (m + 1)
        total = [0] * (m + 1)

        rank = {v: i + 1 for i, v in enumerate(vals)}

        for v in nums[:x]:
            r = rank[v]
            update(count, r, 1)
            update(total, r, v)

        costs = []

        for i in range(n - x + 1):
            mid = kth(count, (x + 1) // 2)
            med = vals[mid - 1]

            c = query(count, mid)
            s = query(total, mid)

            left = med * c - s
            right = (query(total, m) - s) - med * (x - c)

            costs.append(left + right)

            if i < n - x:
                old = rank[nums[i]]
                new = rank[nums[i + x]]

                update(count, old, -1)
                update(total, old, -nums[i])

                update(count, new, 1)
                update(total, new, nums[i + x])

        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]
