from library import BinaryTreeNode, BinarySearchTree

class AvlTree(BinarySearchTree):
    '''
    Override: insert
    '''
    def __init__(self, x):
        '''
        Initializes RB tree from list x
        '''
        self.root = AvlTreeNode(x[0])
        x = x[1:]
        for item in x:
            self.insert(item)

    def insert(self, x):
        '''
        Inserts integer x into AVL
        '''
        if (self.root)
            self._insert_node_helper(AvlTreeNode(x), self.root)
        else:
            self.root = AvlTreeNode(x)

    def _insert_node_helper(self, node, current):
        '''
        Recursive helper to insert node into BST
        '''
        if (node.value > current.value):
            if (current.has_right_children()):
                self.insert_node_helper(node, current.right)
            else:
                current.right = node
                node.parent = current
                self._update_balance_factor(node)
        elif (node.value < current.value):
            if (current.has_left_children()):
                self.insert_node_helper(node, current.left)
            else:
                current.left = node
                node.parent = current
                self._update_balance_factor(node)

    def _update_balance_factor(self, node):
        '''
        Updates the balance factor from node up until root
        '''
        if node.balance_factor > 1 or node.balance_factor < -1:
            self._rebalance(node)
            return
        if (node.parent is None):
            return
        else:
            if (node.is_left_child()):
                node.parent.balance_factor += 1
            elif (node.is_right_child()):
                node.parent.balance_factor -= 1
            if (node.parent.balance_factor != 0)
                self._update_balance_factor(node.parent)

    def _rebalance(self, node):
        '''
        Rebalances tree at node
        case 1: tree is right heavy, in right subtree of pivot
        case 2: '' '' right heavy, in left subtree of pivot
        case 3: '' '' left heavy, in right subtree of pivot
        case 4: '' '' left heavy, in left subtree of pivot
        '''
        if node.parent is None
            return
        # check the cases
        if node.balance_factor < -1:
            if node.right.has_left_child():
                # case 2
                self._right_rotation(node.right)
                self._left_rotation(node)
            else:
                # case 1
        elif node.balance_factor > 1:
            # check
            if node.left.has_left_child():
                self._right_rotation(node)
            else:
                self._left_rotation(node.right)
                self._right_rotation(node)

    def _left_rotation(self, root):
        '''
        Performs left rotation at node
        '''
        if root.right is None:
            raise Exception("Invalid operation, no right child in root")
        new_root = root.right
        root.right = new_root.left

        if new_root.has_left_child():
            new_root.left.parent = root

        # fix root's parent reference
        if root == self.root:
            self.root = new_root
        else:
            if root.is_left_child():
                root.parent.left = new_root
            elif root.is_right_child():
                root.parent.right = new_root

        new_root.left = root
        root.parent = new_root
        # TODO: update the balance factors

    def _right_rotation(self, old_root):
        '''
        Performs right rotation at node
        '''
        if old_root.left is None:
            raise Exception("Invalid operation, no left child in root")
        # establish pivot to be the new root
        new_root = old_root.left
        old_root.left = new_root.right # can be None
        # fix new_root right child's parent reference 
        if new_root.has_right_child():
            new_root.right.parent = old_root

        # fix old_root's parent node's child references
        if old_root == self.root:
            self.root = new_root
        else:
            if old_root.is_left_child():
                old_root.parent.left = new_root
            elif old_root.is_right_child():
                old_root.parent.right = new_root

        # Complete rotation: pivot becomes root, root becomes child of pivot
        new_root.left = old_root
        old_root.parent = new_root
        # TODO: update the balance factors

class AvlTreeNode(BinaryTreeNode):
    def __init__(self, x):
        super.__init__(x)
        self.height = 0
        self.balance_factor = 0
