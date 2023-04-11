from collections import deque


class Vertex:

    def __init__(self, value) -> None:
        self.value = value
        self.adjacent_vertices = []
        # Look up alternative adjacency matrix implementation

    def add_adjacent_vertex(self, vertex):
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        # undirected mutual addition
        vertex.adjacent_vertices.append(self)

class WeightedVertex:

    def __init__(self, value) -> None:
        self.value = value
        self.adjacent_vertices = {}

    def add_adjacent_vertex(self, vertex, weight):
        self.adjacent_vertices[vertex] = weight

def dfs(vertex, search_value, visited_vertices={}):
    if vertex.value == search_value:
        return vertex
    
    visited_vertices[vertex.value] = True

    for v in vertex.adjacent_vertices:
        if visited_vertices[v.value]:
            continue

        if v.value == search_value:
            return v

        searching_for_vertex = dfs(v, search_value, visited_vertices)
        if searching_for_vertex:
            return searching_for_vertex
    return None


def bfs(starting_vertex, search_value):
    visited_vertices = {}
    visited_vertices[starting_vertex.value] = True
    queue = deque()
    queue.append(starting_vertex)

    while len(queue) > 0:
        current_vertex = queue.pop()
        if current_vertex.value == search_value:
            return current_vertex
        
        for vertex in current_vertex.adjacent_vertices:
            if not visited_vertices.get(vertex.value):
                visited_vertices[vertex.value] = True
                queue.append(vertex)
    return None
        
    
def bfs_traverse(starting_vertex):
    queue = deque()

    visited_vertices = {}
    visited_vertices[starting_vertex.value] = True
    queue.append(starting_vertex)

    while len(queue) > 0:
        current_vertex = queue.pop()
        print(current_vertex.value)

        for vertex in current_vertex.adjacent_vertices:
            if not visited_vertices.get(vertex.value):
                visited_vertices[vertex.value] = True
                queue.append(vertex)

def dfs_traverse(vertex, visited_vertices={}):
    visited_vertices[vertex.value] = True
    print(vertex.value)

    for v in vertex.adjacent_vertices:
        if visited_vertices[v]:
            continue
        dfs_traverse(v, visited_vertices)


def shortest_path_for_unweighted_graph(starting_vertex, destination_vertex, visited_vertices={}):
    queue = deque()

    previous_vertex_table = {}

    # Use breadth first search
    visited_vertices[starting_vertex.value] = True
    queue.append(starting_vertex)

    while len(queue) > 1:
        current_vertex = queue.pop()
        
        for vertex in current_vertex.adjacent_vertices:
            if not visited_vertices.get(vertex.value):
                visited_vertices[vertex.value] = True
                queue.append(vertex)
                # Store in the previous vertex table the adjacent vertex as key and current vertex as value
                previous_vertex_table[vertex.value] = current_vertex.value
    
    shortest_path = []
    current_vertex_value = destination_vertex.value
    while current_vertex_value != starting_vertex.value:
        shortest_path.append(current_vertex_value)
        current_vertex_value = previous_vertex_table[current_vertex_value]
    shortest_path.append(starting_vertex)
    return shortest_path[::-1]

    # Could adjust above so that the loop breaks once the shortest path is found rather than traversing the whole graph
        
