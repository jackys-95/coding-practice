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
        if x is None:
            return
        new_node = AvlTreeNode(x)

    def _update_balance_factor(self, x):
        '''
        Updates the balance factor
        '''
        raise NotImplementedError

    def _left_rotation(self, node):
        '''
        Performs left rotation at node
        '''
        raise NotImplementedError

    def _right_rotation(self, node):
        '''
        '''
        raise NotImplementedError


class AvlTreeNode(BinaryTreeNode):
    def __init__(self, x):
        super.__init__(x)
        self.balance_factor = 0
