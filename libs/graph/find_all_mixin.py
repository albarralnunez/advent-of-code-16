from libs.priority_queue import PriorityQueue


class FindAllMixin(object):

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
