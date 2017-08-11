from graph import Graph, Vertex, graph_bfs, graph_dfs

g = Graph()
for i in range(6):
    g.add_vertex(Vertex(i))

g.add_edge(g.vertices[0], g.vertices[1])
g.add_edge(g.vertices[1], g.vertices[2])
g.add_edge(g.vertices[1], g.vertices[3])
g.add_edge(g.vertices[1], g.vertices[4])
g.add_edge(g.vertices[1], g.vertices[5])

#print(g)
print(graph_bfs(g, 5).value)
print(graph_dfs(g, 5).value)
