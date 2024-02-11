import json


class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value


def traverse(node: Node):
    tree = {"value": node.value}
    tree["left"] = None if node.left is None else traverse(node.left)
    tree["right"] = None if node.right is None else traverse(node.right)
    return tree


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        node = self.root
        while True:
            if node.value < value:
                if node.right is None:
                    node.right = Node(value)
                    return
                node = node.right
            else:
                if node.left is None:
                    node.left = Node(value)
                    return
                node = node.left

    def lookup(self, value):
        node = self.root
        while node:
            if node.value == value:
                return node
            elif node.value > value:
                node = node.left
            else:
                node = node.right
        return

    def remove(self, value):
        if self.root is None:
            return

        node = self.root
        parent = None
        while node:
            if node.value > value:
                parent = node
                node = node.left
            elif node.value < value:
                parent = node
                node = node.right
            elif node.value == value:
                if node.right is None:
                    if parent is None:
                        self.root = node.left
                    else:
                        if node.value > parent.value:
                            parent.right = node.left
                        elif node.value < parent.value:
                            parent.left = node.left
                elif node.right.left is None:
                    if parent is None:
                        self.root = node.left
                    else:
                        node.right.left = node.left

                        if node.value > parent.value:
                            parent.right = node.right
                        elif node.value < parent.value:
                            parent.left = node.right
                else:
                    leftmost = node.right.left
                    leftmost_parent = node.right
                    while leftmost.left:
                        leftmost_parent = leftmost
                        leftmost = leftmost.left

                    leftmost_parent.left = leftmost.right
                    leftmost.left = node.left
                    leftmost.right = node.right

                    if parent is None:
                        self.root = leftmost
                    else:
                        if node.value < parent.value:
                            parent.left = leftmost
                        elif node.value > parent.value:
                            parent.right = leftmost
                return


def main() -> None:
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)

    print(json.dumps(traverse(tree.root), indent=3))
    node = tree.lookup(1)
    print(node.value, node.left, node.right)
    print(tree.lookup(30))

    tree.remove(170)
    print(json.dumps(traverse(tree.root), indent=3))


if __name__ == "__main__":
    main()
