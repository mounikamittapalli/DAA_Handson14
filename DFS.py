class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices
        self.graph = {i: [] for i in range(vertices)}  # Adjacency list

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def dfs(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

# Create the graph
graphDFS = Graph(8)

# Add edges
graphDFS.add_edge(0, 1)
graphDFS.add_edge(0, 2)
graphDFS.add_edge(0, 3)
graphDFS.add_edge(1, 3)
graphDFS.add_edge(2, 4)
graphDFS.add_edge(3, 5)
graphDFS.add_edge(3, 6)
graphDFS.add_edge(4, 7)
graphDFS.add_edge(4, 5)
graphDFS.add_edge(5, 2)

# Prepare visited array
visited = [False] * 8

# Perform DFS
print("DFS traversal starting from vertex 0:")
graphDFS.dfs(0, visited)
