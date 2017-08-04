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

    def has_children(self):
        return self.has_left_children() or self.has_right_children()

    def get_children(self):
        children = []
        if self.has_left_children():
            children.append(self.left)
        if self.has_right_children():
            children.append(self.right)
        return children

    def is_left_child(self):
        if self.parent is not None:
            return (True if self.parent.left.value == self.value
                         else False)
        return False

    def is_right_child(self):
        if self.parent is not None:
            return (True if self.parent.right.value == self.value
                         else False)
        return False

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

    def delete_node(self, node):
        '''
        Deletes a node
        TODO: needs a refactor
        '''
        if not node.has_children():
            if node.parent is not None:
                if node.is_left_child():
                    node.parent.left = None
                else:
                    node.parent.right = None
            else:
                self.root = None
        else:
            successor = self.find_successor(node)
            if successor is not None:
                if (node.parent and node.parent.value == successor.value):
                    node.left.parent = successor
                    successor.left = node.left
                else:
                    if (node.parent and node.parent.value != successor.value):
                        # fix node parent's references
                        if node.is_left_child():
                            node.parent.left = successor
                        else:
                            node.parent.right = successor
                    else: # root is being deleted
                        self.root = successor
                    # disconnect successor
                    if successor.is_left_child():
                        successor.parent.left = None
                    else:
                        successor.parent.right = None
                    # fix node child's references
                    if node.has_left_children():
                        node.left.parent = successor
                        successor.left = node.left
                    if (node.has_right_children() and \
                        node.right.value != successor.value):
                        node.right.parent = successor
                        successor.right = node.right
            else: # promote left child
                if node.parent is None:
                    self.root = node.left
                elif node.is_left_child():
                    node.parent.left = node.left
        del node

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

from simplequeue import SimpleQueue

def bt_bfs(root_node, value):
    if (root_node is None):
        return None
    else:
        q = SimpleQueue()
        q.enqueue(root_node)
        while q.is_empty() is False:
            current = q.dequeue()
            if current.value == value:
                return current
            for child in current.get_children():
                q.enqueue(child)
    return None

def bt_dfs(node, value):
    if (node is None):
        return None
    elif (node.value == value):
        return node
    else:
        for child in node.get_children():
            found = bt_dfs(child, value)
            if found is not None:
                return found
    return None
