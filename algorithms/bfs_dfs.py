from data_structures.tree import BinarySearchTree


def traverse_in_order(node, list):
    if node.left:
        traverse_in_order(node.left, list)
    list.append(node.value)
    if node.right:
        traverse_in_order(node.right, list)
    return list


def traverse_pre_order(node, list):
    list.append(node.value)
    if node.left:
        traverse_pre_order(node.left, list)
    if node.right:
        traverse_pre_order(node.right, list)
    return list


def traverse_post_order(node, list):
    if node.left:
        traverse_post_order(node.left, list)
    if node.right:
        traverse_post_order(node.right, list)
    list.append(node.value)
    return list


class BinarySearchTreeMod(BinarySearchTree):
    def __init__(self) -> None:
        super().__init__()

    def bfs(self):
        list = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            list.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return list

    def bfsr(self, queue, list):
        if not queue:
            return list

        node = queue.pop(0)
        list.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        return self.bfsr(queue, list)

    def dfs_in_order(self):
        return traverse_in_order(self.root, [])

    def dfs_pre_order(self):
        return traverse_pre_order(self.root, [])

    def dfs_post_order(self):
        return traverse_post_order(self.root, [])

    def validate(self):
        queue = [(self.root, None, None)]
        while queue:
            node, lower, upper = queue.pop(0)

            if (lower is not None and node.value <= lower) or (upper is not None and node.value >= upper):
                return False

            if node.left:
                queue.append((node.left, lower, node.value if upper is None or node.value < upper else upper))

            if node.right:
                queue.append((node.right, node.value if lower is None or node.value > lower else lower, upper))

        return True


def main() -> None:
    #       9
    #   4       20
    # 1   6   15   170
    tree = BinarySearchTreeMod()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)

    # print(tree.bfs())
    # print(tree.bfsr([tree.root], []))

    print(tree.dfs_in_order())
    print(tree.dfs_pre_order())
    print(tree.dfs_post_order())

    tree.root.right.value = 14
    print(tree.validate())


if __name__ == "__main__":
    main()
