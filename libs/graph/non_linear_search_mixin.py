from libs.priority_queue import PriorityQueue


class NonLinearSearchMixin(object):

    def non_linear_search(self, start, goal):
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
                cost_so_far[neighbour] = new_cost
                priority = new_cost
                frontier.push(neighbour, priority)
                came_from[neighbour] = current
        return came_from, cost_so_far
