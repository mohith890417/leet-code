class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.sum_sq = [0] * (4 * n)
        self.MOD = 10**9 + 7

    def _push(self, node, left, right):
        if self.lazy[node] != 0:
            val = self.lazy[node]
            mid = (left + right) // 2
            
            # Apply to left child
            self._apply(2 * node, left, mid, val)
            # Apply to right child
            self._apply(2 * node + 1, mid + 1, right, val)
            
            self.lazy[node] = 0

    def _apply(self, node, left, right, val):
        length = right - left + 1
        # sum((x + val)^2) = sum(x^2) + 2*val*sum(x) + val^2 * length
        self.sum_sq[node] = (
            self.sum_sq[node] + 
            2 * val * self.tree[node] + 
            val * val * length
        ) % self.MOD
        
        self.tree[node] = (self.tree[node] + val * length) % self.MOD
        self.lazy[node] = (self.lazy[node] + val) % self.MOD

    def update(self, node, left, right, q_left, q_right, val):
        if q_left > right or q_right < left:
            return
        if q_left <= left and right <= q_right:
            self._apply(node, left, right, val)
            return

        self._push(node, left, right)
        mid = (left + right) // 2
        self.update(2 * node, left, mid, q_left, q_right, val)
        self.update(2 * node + 1, mid + 1, right, q_left, q_right, val)
        
        self.sum_sq[node] = (self.sum_sq[node, 2 * node] + self.sum_sq[2 * node + 1]) % self.MOD
        self.tree[node] = (self.tree[2 * node] + self.tree[2 * node + 1]) % self.MOD

    def update(self, node, left, right, q_left, q_right, val):
        if q_left > right or q_right < left:
            return
        if q_left <= left and right <= q_right:
            self._apply(node, left, right, val)
            return
        
        self._push(node, left, right)
        mid = (left + right) // 2
        self.update(2 * node, left, mid, q_left, q_right, val)
        self.update(2 * node + 1, mid + 1, right, q_left, q_right, val)
        
        self.sum_sq[node] = (self.sum_sq[2 * node] + self.sum_sq[2 * node + 1]) % self.MOD
        self.tree[node] = (self.tree[2 * node] + self.tree[2 * node + 1]) % self.MOD

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        tree = SegmentTree(n)
        
        last_seen = {}
        total_sum = 0
        current_sum_sq = 0
        
        for i, x in enumerate(nums):
            prev = last_seen.get(x, -1)
            last_seen[x] = i
            
            # Update range [prev + 1, i] with +1
            tree.update(1, 0, n - 1, prev + 1, i, 1)
            
            # The total sum of squares of all subarrays ending at index i 
            # is stored at the root of the segment tree (representing range [0, i])
            total_sum = (total_sum + tree.sum_sq[1]) % MOD
            
        return total_sum
        