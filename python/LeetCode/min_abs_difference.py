# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        inorder_list = inorder_traversal(root)
        print(inorder_traversal)

        
def inorder_traversal(root_node):
    result = []
    if (root_node != None):
        result += inorder_traversal(root_node.left)
        result += root_node.value 
        result += inorder_traversal(root_node.right)
    return result