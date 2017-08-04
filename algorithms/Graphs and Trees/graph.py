class Graph:
    '''
    Directed graph which can only contain unique vertices
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
