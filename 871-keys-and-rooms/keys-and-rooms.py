class Solution:
    def canVisitAllRooms(self, rooms: List[int]) -> bool:
        visited = set()

        def dfs(room: int):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)

        # Start DFS traversal from room 0
        dfs(0)

        # Return True if we were able to visit all rooms
        return len(visited) == len(rooms)