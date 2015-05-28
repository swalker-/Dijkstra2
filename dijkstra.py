__author__ = 'Stephen'

import collections

Coordinate = collections.namedtuple('Coordinate', ['row', 'column'])
Node = collections.namedtuple('Node', ['parent', 'coordinate', 'distance'])

__no_path = -1

def bfs(graph, start, destination):
    stack = collections.deque()
    stack.appendleft(Node('root', start, 0))
    visited = [start]
    path_graph = __setup_path_graph(graph)
    result = __find_shortest_path(graph, destination, stack, visited, path_graph)
    if result == __no_path:
        return __no_path, path_graph
    path = collections.deque()
    path.appendleft(result.coordinate)
    current_node = result.parent
    while current_node.parent != 'root':
        path.appendleft(current_node.coordinate)
        current_node = current_node.parent
    return path, path_graph

def __setup_path_graph(graph):
    path_graph = [['.' for x in range(len(graph[0]))] for x in range(len(graph))]
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if graph[row][col] == -1:
                path_graph[row][col] = 'X'
    return path_graph

def __find_shortest_path(graph, destination, stack, visited, path_graph):
    if len(stack) == 0:
        return __no_path
    current = stack.pop()
    path_graph[current.coordinate.row][current.coordinate.column] = current.distance
    if current.coordinate == destination:
        return current
    coord = current.coordinate
    potential_coordinates = [Coordinate(coord.row-1, coord.column), Coordinate(coord.row+1, coord.column),
                             Coordinate(coord.row, coord.column-1), Coordinate(coord.row, coord.column+1)]
    for coordinate in potential_coordinates:
        if __valid_coordinate(graph, coordinate, visited):
            new_node = Node(current, coordinate, current.distance+1)
            visited.append(coordinate)
            stack.appendleft(new_node)
    return __find_shortest_path(graph, destination, stack, visited, path_graph)


def __valid_coordinate(graph, coordinate, visited):
    valid_row = __valid_property(coordinate.row, len(graph))
    valid_col = __valid_property(coordinate.column, len(graph[0]))

    if valid_row and valid_col and (coordinate not in visited):
        return graph[coordinate.row][coordinate.column] != -1
    return False

def __valid_property(p, max_value):
    return 0 <= p < max_value
