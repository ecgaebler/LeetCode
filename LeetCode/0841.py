class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque()
        queue.append(0)
        while queue:
            room = queue.popleft()
            visited.add(room)
            keys = rooms[room]
            for key in keys:
                if key not in visited:
                    queue.append(key)
        return len(visited) == len(rooms)