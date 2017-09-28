class Solution(object):
    def __init__(self):
        self.inorder_list = None
    
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.inorder_list = inorder_traversal_list(root)
        self.inorder_traversal(root)
        return root

    def inorder_traversal(self, root_node):
        if (root_node != None):
            self.inorder_traversal(root_node.left)
            root_node.val = sum(self.inorder_list)
            self.inorder_list = self.inorder_list[1:]
            self.inorder_traversal(root_node.right)
            
def inorder_traversal_list(root_node):
    result = []
    if (root_node != None):
        result += inorder_traversal_list(root_node.left)
        result += [root_node.val]
        result += inorder_traversal_list(root_node.right)
    return result