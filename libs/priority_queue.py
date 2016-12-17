import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, item))

    def pop(self):
        return heapq.heappop(self._queue)[1]
