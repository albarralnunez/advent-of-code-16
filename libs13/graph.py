from libs.priority_queue import PriorityQueue


class Node(object):

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

    def find_all(self, start, steps):
        frontier = PriorityQueue()
        frontier.push(start, 0)
        came_from = {start: None}
        cost_so_far = {start: 0}
        while len(frontier) != 0:
            current = frontier.pop()
            for neighbour in current.neighbors:
                new_cost = (cost_so_far[current] +
                            self.movement_cost(current, neighbour))
                if (neighbour not in cost_so_far or
                        new_cost < cost_so_far[neighbour]):
                    cost_so_far[neighbour] = new_cost
                    priority = new_cost
                    if priority < steps:
                        frontier.push(neighbour, priority)
                    came_from[neighbour] = current
        return came_from, cost_so_far

    def a_star_search(self, start, goal):
        frontier = PriorityQueue()
        frontier.push(start, 0)
        came_from = {start: None}
        cost_so_far = {start: 0}
        while len(frontier) != 0:
            current = frontier.pop()
            if current == goal:
                break
            for neighbour in current.neighbors:
                new_cost = (cost_so_far[current] +
                            self.movement_cost(current, neighbour))
                if (neighbour not in cost_so_far or
                        new_cost < cost_so_far[neighbour]):
                    cost_so_far[neighbour] = new_cost
                    priority = new_cost + self.heuristic(goal, neighbour)
                    frontier.push(neighbour, priority)
                    came_from[neighbour] = current
        return came_from, cost_so_far

    def dijkstra_search(self, start, goal):
        frontier = PriorityQueue()
        frontier.push(start, 0)
        came_from = {start: None}
        cost_so_far = {start: 0}
        while len(frontier) != 0:
            current = frontier.pop()
            if current == goal:
                break
            for neighbour in current.neighbors:
                new_cost = (cost_so_far[current] +
                            self.movement_cost(current, neighbour))
                if (neighbour not in cost_so_far or
                        new_cost < cost_so_far[neighbour]):
                    cost_so_far[neighbour] = new_cost
                    priority = new_cost
                    frontier.push(neighbour, priority)
                    came_from[neighbour] = current
        return came_from, cost_so_far

    @staticmethod
    def reconstruct_path(came_from, start, goal):
        current = goal
        path = [current]
        while current != start:
            current = came_from[current]
            path.append(current)
        path.reverse()  # optional
        return path
