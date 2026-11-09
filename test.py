# BFS SEARCH FROM STARTING NODE A TO GOAL NODE G
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj = [[] for _ in range(len(nodes))]

    def addEdge(self, u, v):
        i = self.nodes.index(u)
        self.adj[i].append(v)

    def bfs(self, start, goal):
        visited = [start]
        queue = [start]

        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            if node == goal:
                print("\nGoal found!")
                return

            i = self.nodes.index(node)

            for neighbour in self.adj[i]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

        print("\nGoal not found!")


nodes = ['A', 'B', 'F', 'D', 'E', 'K', 'J',
         'G', 'C', 'H', 'I', 'N', 'M', 'L']

g = Graph(nodes)

g.addEdge('A', 'B')
g.addEdge('A', 'F')
g.addEdge('A', 'D')
g.addEdge('A', 'E')

g.addEdge('B', 'K')
g.addEdge('B', 'J')

g.addEdge('D', 'G')

g.addEdge('E', 'C')
g.addEdge('E', 'H')
g.addEdge('E', 'I')

g.addEdge('K', 'N')
g.addEdge('K', 'M')

g.addEdge('I', 'L')

g.bfs('A', 'G')
