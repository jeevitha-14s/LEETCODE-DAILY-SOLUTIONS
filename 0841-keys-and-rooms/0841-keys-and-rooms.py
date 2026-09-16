class Solution:
        def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
            seen = {0}
            stack = [0]
            while stack:
                for k in rooms[stack.pop()]:
                    if k not in seen:
                        seen.add(k)
                        stack.append(k)
            return len(seen) == len(rooms)