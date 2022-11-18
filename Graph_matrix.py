from Vertex_martrix import Vertex_martrix

class Graph_matrix:
    vertices = {}
    edges = []
    edge_indexes = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex_martrix) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indexes[vertex.name] = len(self.edge_indexes)
            return True
        else:
            return False
    
    def add_edge(self, u, v, weight = 1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indexes[u]][self.edge_indexes[v]] = weight
            self.edges[self.edge_indexes[v]][self.edge_indexes[u]] = weight
            return True
        else:
            return False
        
    def print_graph(self):
        for v, i in sorted(self.edge_indexes.items()):
            print(v + ' ', end='')
            for j in range(len(self.edges)):
               print(self.edges[i][j], end=' ')
            print(' ')


