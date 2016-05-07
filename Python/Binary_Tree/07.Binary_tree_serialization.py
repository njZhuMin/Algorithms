"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import collections
class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root):
        if not root:
            return
        ret = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                ret.append(str(node.val))
            else:
                ret.append('#')

        return ','.join(ret)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """
    def deserialize(self, data):
        if not data:
            return
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        i = 1
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if nodes[i] == '#':
                node.left = None
            else:
                t = TreeNode(int(nodes[i]))
                node.left = t
                queue.append(t)
            i += 1

            if nodes[i] == '#':
                node.right = None
            else:
                t = TreeNode(int(nodes[i]))
                node.right = t
                queue.append(t)
            i += 1

        return root
