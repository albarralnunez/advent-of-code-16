

class Node(object):

    def __repr__(self):
        return str(self.node_id)

    @property
    def node_id(self):
        raise NotImplementedError

    @property
    def neighbors(self):
        raise NotImplementedError


class Graph(object):

    @property
    def _graph(self):
        raise NotImplemented

    def heuristic(self, a, b):
        raise NotImplementedError

    def movement_cost(self, a, b):
        raise NotImplementedError

    @staticmethod
    def reconstruct_path(came_from, start, goal):
        current = goal
        path = [current]
        while current != start:
            current = came_from[current]
            path.append(current)
        path.reverse()  # optional
        return path
