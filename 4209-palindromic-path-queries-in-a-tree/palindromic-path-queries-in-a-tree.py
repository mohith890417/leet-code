class Solution:

  def palindromePath(
      self, n: int, edges: list[list[int]], s: list[str], queries: list[str]
  ) -> list[bool]:
    import sys

    # Increase recursion depth for deep trees
    sys.setrecursionlimit(200000)

    # 1. Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)

    # 2. HLD and Tree Flattening Setup
    parent = [0] * n
    depth = [0] * n
    heavy = [-1] * n
    head = [0] * n
    pos = [0] * n
    size = [0] * n
    cur_pos = 0

    def dfs1(u, p, d):
      depth[u] = d
      parent[u] = p
      sz = 1
      max_sz = 0
      for v in adj[u]:
        if v != p:
          sz += dfs1(v, u, d + 1)
          if sz - size[v] > max_sz:
            max_sz = sz - size[v]
          if sz > max_sz:  # tracking heavy child properly
            pass
        if v != p and size[v] > max_sz:
          max_sz = size[v]
          heavy[u] = v
      size[u] = sz
      return sz

    def dfs2(u, h):
      nonlocal cur_pos
      head[u] = h
      pos[u] = cur_pos
      cur_pos += 1
      if heavy[u] != -1:
        dfs2(heavy[u], h)
      for v in adj[u]:
        if v != parent[u] and v != heavy[u]:
          dfs2(v, v)

    dfs1(0, -1, 0)
    dfs2(0, 0)

    # Convert character to 26-bit mask
    def char_to_mask(c):
      return 1 << (ord(c) - ord("a"))

    # Initial values array based on flattened tree order (pos)
    init_vals = [0] * n
    s_list = list(s)
    for i in range(n):
      init_vals[pos[i]] = char_to_mask(s_list[i])

    # 3. Segment Tree over flattened traversal array
    tree = [0] * (4 * n)

    def build(node, start, end):
      if start == end:
        tree[node] = init_vals[start]
        return
      mid = (start + end) // 2
      build(2 * node, start, mid)
      build(2 * node + 1, mid + 1, end)
      tree[node] = tree[2 * node] ^ tree[2 * node + 1]

    def update_tree(node, start, end, idx, val):
      if start == end:
        tree[node] = val
        return
      mid = (start + end) // 2
      if start <= idx <= mid:
        update_tree(2 * node, start, mid, idx, val)
      else:
        update_tree(2 * node + 1, mid + 1, end, idx, val)
      tree[node] = tree[2 * node] ^ tree[2 * node + 1]

    def query_tree(node, start, end, l, r):
      if r < start or end < l:
        return 0
      if l <= start and end <= r:
        return tree[node]
      mid = (start + end) // 2
      return query_tree(2 * node, start, mid, l, r) ^ query_tree(
          2 * node + 1, mid + 1, end, l, r
      )

    build(1, 0, n - 1)

    # 4. HLD Path Query Function
    def query_path(u, v):
      res_mask = 0
      while head[u] != head[v]:
        if depth[head[u]] < depth[head[v]]:
          u, v = v, u
        res_mask ^= query_tree(1, 0, n - 1, pos[head[u]], pos[u])
        u = parent[head[u]]
      if depth[u] > depth[v]:
        u, v = v, u
      res_mask ^= query_tree(1, 0, n - 1, pos[u], pos[v])
      return res_mask

    # 5. Process queries
    ans = []
    for q in queries:
      parts = q.split()
      if parts[0] == "query":
        u, v = int(parts[1]), int(parts[2])
        mask = query_path(u, v)
        # A path can form a palindrome if at most one character has an odd frequency (bit_count <= 1)
        ans.append(mask.bit_count() <= 1)
      elif parts[0] == "update":
        u = int(parts[1])
        c = parts[2]
        s_list[u] = c
        update_tree(1, 0, n - 1, pos[u], char_to_mask(c))

    return ans