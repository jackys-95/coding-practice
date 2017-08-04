from graph import Graph, Vertex

g = Graph()
for i in range(6):
    g.add_vertex(Vertex(i))

g.add_edge(g.vertices[1], g.vertices[2])
g.add_edge(g.vertices[1], g.vertices[3])
print(g)
