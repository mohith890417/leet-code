from collections import defaultdict, deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Adjacency list: store neighbor and direction cost (1 if original edge, 0 if reversed)
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append((v, 1))  # 1 means direction is u -> v (needs reversal if traversed u -> v)
            adj[v].append((u, 0))  # 0 means direction is v -> u (already points towards parent/0)
            
        visited = [False] * n
        changes = 0
        
        # BFS starting from city 0
        queue = deque([0])
        visited[0] = True
        
        while queue:
            curr = queue.popleft()
            
            for neighbor, cost in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    changes += cost
                    queue.append(neighbor)
                    
        return changes