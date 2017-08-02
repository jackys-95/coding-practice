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
        Finds the predecessor of node
        '''
        if not(node.parent): # node is root
            return find_max_from(node)
        elif (node.value < node.parent.value):
            if not(node.has_left_children()):
                # handle case where node is in right subtree of root
                if (node.value > self.root.value):
                    return self.root
                else:
                    return None
            else:
                return self.find_max_from(node.left)
        elif (node.value > node.parent.value):
            if not(node.has_left_children()):
                # handle case where node is in right subtree of root
                if (node.value > self.root.value):
                    return self.root
                else:
                    return node.parent
            else:
                return self.find_max_from(node.left)

    def find_max_from(self, node):
        '''
        Finds the max value inside bst
        starting from node
        '''
        current = node
        while(current.has_right_children()):
            current = current.right
        return current

    def find_successor(self, node):
        '''
        Finds the successor of node
        '''
        if not(node.parent): # node is root
            if not(node.has_right_children()):
                return None
            else:
                return self.find_min_from(node.right)
        elif (node.value < node.parent.value):
            if node.has_right_children():
                if (node.right.has_left_children()):
                    self.find_min_from(node.right)
                else:
                    return node.right
            else:
                return node.parent
        elif (node.value > node.parent.value):
            if not(node.has_right_children()):
                if node.parent.parent is None:
                    return None
                elif (node.parent.value < node.parent.parent.value):
                    return node.parent.parent
            else:
                return node.right

    def find_min_from(self, node):
        '''
        Finds the min value inside bst
        starting from node
        '''
        current = node
        while(current.has_left_children()):
            current = current.left
        return current
    
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

source = [70, 31, 93, 94, 14, 23, 73]
print(source)
bst = BinarySearchTree(source)
child = bst.get_right_child()
child2 = child.left
child3 = bst.find_min_from(bst.root)
print("Predecessor of " + str(child.value) + " is " + \
      str(bst.find_predecessor(child).value))
print("Predecessor of " + str(child2.value) + " is " + \
      str(bst.find_predecessor(child2).value))

predecessor_child3 = bst.find_predecessor(child3)
if predecessor_child3 is None:
    print(str(child3.value) + " has no predecessor")

print("Successor of " + str(child.value) + " is " + \
      str(bst.find_successor(child).value))
print("Successor of " + str(child2.value) + " is " + \
      str(bst.find_successor(child2).value))

child4 = bst.find_max_from(bst.root)
successor_child4 = bst.find_successor(child4)
if successor_child4 is None:
    print(str(child4.value) + " has no successor")

child5 = child3.right
print("Successor of " + str(child5.value) + " is " + \
      str(bst.find_successor(child5).value))
