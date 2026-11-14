class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        adjacency_list = collections.defaultdict(dict)
        
        # Step 1: Build the graph
        for (u, v), val in zip(equations, values):
            adjacency_list[u][v] = val
            adjacency_list[v][u] = 1.0 / val
            
        # Step 2: DFS function to find the path product from start to target
        def dfs(start, target, visited):
            if start == target:
                return 1.0
            visited.add(start)
            
            for neighbor, weight in adjacency_list[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited)
                    if result != -1.0:
                        return weight * result
                        
            return -1.0

        # Step 3: Process all queries
        answers = []
        for c, d in queries:
            if c not in adjacency_list or d not in adjacency_list:
                answers.append(-1.0)
            elif c == d:
                answers.append(1.0)
            else:
                answers.append(dfs(c, d, set()))
                
        return answers