import json


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        def preorder_traversal(node):
            if node is None:
                preorder.append(None)
                return
            preorder.append(node.val)
            preorder_traversal(node.left)
            preorder_traversal(node.right)

        preorder = []
        preorder_traversal(root)
        return json.dumps(preorder)

    def deserialize(self, data: str):
        def build_tree_helper(preorder):
            if preorder[idx[0]] is None:
                return None
            node = TreeNode(preorder[idx[0]])
            idx[0] += 1
            node.left = build_tree_helper(preorder)
            idx[0] += 1
            node.right = build_tree_helper(preorder)
            return node

        idx = [0]
        preorder = json.loads(data)
        return build_tree_helper(preorder)

    def deserialize2(self, data: str):
        def build_tree_helper(preorder):
            if (val := preorder.pop()) is None:
                return None
            node = TreeNode(val)
            node.left = build_tree_helper(preorder)
            node.right = build_tree_helper(preorder)
            return node

        preorder = json.loads(data)
        return build_tree_helper(preorder[::-1])


class Codec2:
    MARKER = "M"

    def serialize(self, root):
        def serialize_rec(node, stream):
            nonlocal m
            if node is None:
                stream.append(self.MARKER + str(m))
                m += 1
                return
            stream.append(node.val)
            serialize_rec(node.left, stream)
            serialize_rec(node.right, stream)

        m = 1
        stream = []
        serialize_rec(root, stream)
        return json.dumps(stream)

    def deserialize(self, data):
        def deserialize_helper(stream):
            val = stream.pop()
            if type(val) is str and val[0] == self.MARKER:
                return None
            node = TreeNode(val)
            node.left = deserialize_helper(stream)
            node.right = deserialize_helper(stream)
            return node

        stream = json.loads(data)
        stream.reverse()
        node = deserialize_helper(stream)
        return node


def main() -> None:
    # ([3, 2, 3, 4], [3, 2, 3, 4])
    inputs = [
        TreeNode(1, left=TreeNode(2), right=TreeNode(3, left=TreeNode(4), right=TreeNode(5))),
        TreeNode(3, left=TreeNode(2, left=TreeNode(3)), right=TreeNode(4)),
    ]
    ser = Codec()
    deser = Codec()
    for root in inputs:
        ans = deser.deserialize2(ser.serialize(root))
        print(ans)


if __name__ == "__main__":
    main()
