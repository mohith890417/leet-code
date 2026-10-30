from typing import List
import heapq


class Solution:
    def shortestPath(
        self,
        n: int,
        edges: List[List[int]],
        labels: str,
        k: int
    ) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        INF = float("inf")

        # dist[node][run_length] = minimum cost
        dist = [[INF] * (k + 1) for _ in range(n)]

        # The path initially contains node 0.
        dist[0][1] = 0

        # (cost, node, current_run_length)
        heap = [(0, 0, 1)]

        while heap:
            cost, u, run_length = heapq.heappop(heap)

            if cost != dist[u][run_length]:
                continue

            if u == n - 1:
                return cost

            for v, weight in graph[u]:
                if labels[u] == labels[v]:
                    next_run_length = run_length + 1
                else:
                    next_run_length = 1

                if next_run_length > k:
                    continue

                next_cost = cost + weight

                if next_cost < dist[v][next_run_length]:
                    dist[v][next_run_length] = next_cost
                    heapq.heappush(
                        heap,
                        (next_cost, v, next_run_length)
                    )

        return -1
