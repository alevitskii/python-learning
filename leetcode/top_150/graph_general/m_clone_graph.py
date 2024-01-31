# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return None

        def dfs(node, seen):
            new_node = Node(node.val)
            seen[new_node.val] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(seen[neighbor.val] if neighbor.val in seen else dfs(neighbor, seen))
            return new_node

        return dfs(node, {})


if __name__ == "__main__":
    node11 = Node(1)
    node12 = Node(2)
    node13 = Node(3)
    node14 = Node(4)
    node11.neighbors = [node12, node14]
    node12.neighbors = [node11, node13]
    node13.neighbors = [node12, node14]
    node14.neighbors = [node11, node13]

    node21 = Node(1)

    inputs = [node11, node21, None]
    s = Solution()
    for node in inputs:
        new_node = s.cloneGraph(node)
        print(new_node)
