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