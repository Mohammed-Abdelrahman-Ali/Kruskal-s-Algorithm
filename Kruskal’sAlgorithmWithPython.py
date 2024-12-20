class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])  # Path compression
        return self.parent[vertex]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(vertices, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])  # Each edge is (u, v, weight)
    
    ds = DisjointSet(vertices)
    mst = []

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            mst.append((u, v, weight))
            ds.union(u, v)

    return mst

# Example Usage
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    ('A', 'B', 1),
    ('A', 'C', 5),
    ('B', 'C', 4),
    ('B', 'D', 2),
    ('C', 'D', 6),
    ('D', 'E', 3)
]

mst = kruskal(vertices, edges)
print("Minimum Spanning Tree:", mst)
