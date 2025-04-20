class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))  # Initially, each vertex is its own parent
        self.rank = [0] * n  # Rank of each node (used for union by rank)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


class Kruskal:
    def __init__(self, vertices, edges):
        self.vertices = vertices  # Number of vertices
        self.edges = edges  # List of edges [(weight, u, v)]

    def kruskal_mst(self):
        # Sort edges based on their weight
        self.edges.sort(key=lambda edge: edge[0])

        # Initialize the disjoint set (Union-Find)
        ds = DisjointSet(self.vertices)

        mst = []  # List to store the edges in the MST
        mst_weight = 0  # Total weight of the MST

        for weight, u, v in self.edges:
            # If u and v belong to different components, include this edge in the MST
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                mst.append((u, v, weight))
                mst_weight += weight

        return mst, mst_weight


# Example usage:
edges = [
    (4, 0, 1),
    (8, 0, 7),
    (11, 1, 7),
    (8, 1, 2),
    (7, 7, 8),
    (1, 6, 7),
    (6, 6, 8),
    (2, 2, 8),
    (4, 2, 5),
    (7, 2, 3),
    (2,6,5),
    (14, 5, 3),
    (10, 5, 4),
    (9, 3, 4)
]

# Number of vertices is 9, edges as a list of (weight, u, v)
g = Kruskal(9, edges)
mst, mst_weight = g.kruskal_mst()

print("Edges in MST:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} with weight {edge[2]}")

print(f"Total weight of MST: {mst_weight}")

