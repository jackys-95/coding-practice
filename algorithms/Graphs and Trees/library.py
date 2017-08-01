class Graph:
    def __init__(self):
        self.nodes = []

class Node:
    def __init__(self):
        self.value = 0
        self.neighbours = []

class BinaryTreeNode:
    '''
    Represents a node of a Binary Tree.
    '''
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
        self.parent = None # for use in BST predecessor/successor

    def has_left_children(self):
        return not(self.left == None)

    def has_right_children(self):
        return not(self.right == None)

class BinaryTree:
    '''
    Represents the root of a Binary Tree
    '''
    def __init__(self, root_node):
        self.root = root_node

    def get_root_value(self):
        return root.value

    def get_left_child(self):
        return self.root.left

    def get_right_child(self):
        return self.root.right

    def insert_node_left(self, new_node):
        '''
        TODO: Ensure new_node has no left children
        '''
        if (self.root.left == None):
            self.root.left = new_node
        else:
            new_node.left = self.root.left
            self.root.left = new_node

    def insert_node_right(self, new_node):
        '''
        TODO: Ensure new_node has no right children
        '''
        if (self.root.right == None):
            self.root.right = new_node
        else:
            new_node.right = self.root.right
            self.root.right = new_node

class BinarySearchTree:
    def __init__(self, x):
        '''
        x is list of integers
        '''
        self.root = BinaryTreeNode(x[0])
        x = x[1:]
        while(len(x) > 0):
            self.insert_node(BinaryTreeNode(x[0]))
            x = x[1:]

    def get_left_child(self):
        return self.root.left

    def get_right_child(self):
        return self.root.right

    def insert_node(self, node):
        '''
        Recursive implementation
        TODO: Handle duplicate values
        '''
        if (self.root):
            self.insert_node_helper(node, self.root)
        else:
            self.root = node
            
    def insert_node_helper(self, node, current):
        '''
        Recursive helper to find correct place in tree
        '''
        if (node.value > current.value):
            if (current.has_right_children()):
                self.insert_node_helper(node, current.right)
            else:
                current.right = node
                node.parent = current
        elif (node.value < current.value):
            if (current.has_left_children()):
                self.insert_node_helper(node, current.left)
            else:
                current.left = node
                node.parent = current

    def find_predecessor(self, node):
        '''
        Incomplete
        '''
        if not(node.parent): # root
            current = node
            while(current.has_right_children()):
                current = current.right
            if (current.has_left_children()):
                return current.left
            else:
                return current
        elif (node.value > node.parent.value):
            if (node.has_left_children()):
                if (node.left.has_right_children()):
                    find_max_from(node)
                else:
                    return node.parent
        #elif (node.value < node.parent.value):

    def find_max_from(self, node):
        '''
        Finds the max value starting from a node
        '''
    
def inorder_traversal(root_node):
    if (root_node != None):
        inorder_traversal(root_node.left)
        print(root_node.value)
        inorder_traversal(root_node.right)

def preorder_traversal(root_node):
    if (root_node != None):
        print(root_node.value)
        preorder_traversal(root_node.left)
        preorder_traversal(root_node.right)

def postorder_traversal(root_node):
    if (root_node != None):
        postorder_traversal(root_node.left)
        postorder_traversal(root_node.right)
        print(root_node.value)

bt = BinaryTree(BinaryTreeNode("A"))
bt.insert_node_left(BinaryTreeNode("B"))
bt.insert_node_right(BinaryTreeNode("C"))

bst = BinarySearchTree([70,31,93,94,14,23,73])
child = bst.get_right_child()
child2 = child.left
print(bst.find_predecessor(child).value)
print(bst.find_predecessor(child2).value)
