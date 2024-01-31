class UnionFind:
    # Initializing the parent list and count variable by traversing the grid
    def __init__(self, grid):
        self.parent = []
        self.rank = []
        self.count = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent.append(i * n + j)
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(1)

    # Function to find the root parent of a node
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    # Function to connect components
    def union(self, v1, v2):
        p1 = self.find(v1)
        p2 = self.find(v2)
        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
            elif self.rank[p1] < self.rank[p2]:
                self.parent[p1] = p2
            else:
                self.parent[p2] = p1
                self.rank[p1] += 1
            self.count -= 1

    # Function to return the number of conencted components consisting of "1"s
    def get_count(self):
        return self.count
