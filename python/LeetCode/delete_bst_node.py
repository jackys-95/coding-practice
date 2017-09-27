#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None

        # find the correct node
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            replace_node = self.findMinLeft(root.right)
            root.val = replace_node.val
            root.right = self.deleteNode(root.right, root.val)

        return root

    def findMinLeft(self, root):
        if root is None:
            return None
        elif root.left is None:
            return root
        else:
            return self.findMinLeft(root.left)


sol = Solution()
tree = TreeNode(5)
tree.left = TreeNode(3)
tree.left.left = TreeNode(2)
tree.left.right = TreeNode(4)
tree.right = TreeNode(6)
tree.right.right = TreeNode(7)
