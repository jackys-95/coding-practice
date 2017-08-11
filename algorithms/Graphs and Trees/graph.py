class Graph:
    '''
    Directed graph which can only contain unique vertices
    TODO: Connectedness?
    '''
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex.value] = vertex

    def __str__(self):
        x = ""
        x += "Vertices: " + str(list(self.vertices.keys())) + "\n"
        for vertex in self.vertices:
            for neighbour in self.vertices[vertex].get_neighbours():
                x += "Vertex " + str(vertex) + \
                     " is connected to " + str(neighbour) + "\n"
        return x[:-1] # cut last newline

    def add_edge(self, from_vert, to_vert):
        '''
        Connects from_vert to to_vert
        '''
        if from_vert.value not in self.vertices:
            vertices[from_vert.value] = from_vert
        elif to_vert.value not in self.vertices:
            vertices[to_vert] = to_vert
        from_vert.add_neighbour(to_vert)

    def get_vertex(self, value):
        '''
        Gets the vertex with given value
        '''
        return (self.vertices[vertex_value]
                if vertex_value in self.vertices
                else None)

    def get_all_vertices(self):
        return self.vertices

class Vertex:
    '''
    Implementing a vertex with adjacency list and dictionary
    for neighbours (uniqueness)
    '''
    def __init__(self, value):
        self.value = value
        self.neighbours = {} # outward neighbours

    def add_neighbour(self, vertex):
        self.neighbours[vertex.value] = vertex

    def get_neighbours(self):
        return self.neighbours

from simplequeue import SimpleQueue

def graph_bfs(graph, value):
    '''
    BFS on a connected graph for value
    '''
    if graph is None:
        return

    vertices = graph.get_all_vertices()
    if len(vertices) == 0:
        return

    q = SimpleQueue()
    q.enqueue(vertices[list(vertices.keys())[0]])

    while q.is_empty() is False:
        current = q.dequeue()
        if current.value == value:
            return current
        for neighbour in current.get_neighbours().values():
            q.enqueue(neighbour)
    return None

def graph_dfs(graph, value):
    '''
    DFS on a connected graph for value
    '''
    if graph is None:
        return

    vertices = graph.get_all_vertices()
    if len(vertices) == 0:
        return

    return _graph_dfs(vertices[list(vertices.keys())[0]], value)

def _graph_dfs(vertex, value):
    '''
    Recursive DFS helper
    '''
    if vertex is None:
        return
    elif vertex.value == value:
        return vertex
    elif len(vertex.get_neighbours()) == 0:
        return
    else:
        for neighbour in vertex.get_neighbours().values():
            found = _graph_dfs(neighbour, value)
            if found is not None:
                return found
    return None
