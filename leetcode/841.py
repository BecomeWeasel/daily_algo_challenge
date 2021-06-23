class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        num_rooms = len(rooms)

        visit = set()

        # set이 visit 리스트보다 더 빠름
        # visit=[False for _ in range(num_rooms)]

        def dfs(room):
            visit.add(room)
            for key in rooms[room]:
                if key not in visit:
                    dfs(key)

        dfs(0)

        return True if len(visit) == num_rooms else False
