from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # adjacency list
        self.V = vertices               # number of vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)
        stack.append(v)  # push to stack when all neighbors are visited

    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        stack.reverse()  # reverse the stack to get the correct order
        return stack

# Example usage:
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 1)
g.add_edge(4, 3)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)


print("Topological Sort:", g.topological_sort())

