from graph import Vertex
from simplestack import SimpleStack

class Trie:
    '''
    Alphabet trie
    '''
    def __init__(self):
        self.root = TrieNode(".") # to signify root node

    def add(self, item):
        '''
        Adds a prefix to the trie
        '''
        item = item.lower()
        tokens = list(item)
        current_node = self.root

        for token in tokens:
            if token not in current_node.children:
                new_node = TrieNode(token)
                current_node.children[token] = new_node
                current_node = new_node
            else:
                current_node = current_node.children[token]
        current_node.is_leaf = True # set the last item to be a leaf

    def is_member(self, item):
        '''
        Checks the trie for a certain prefix
        '''
        item = item.lower()
        tokens = list(item)
        current_node = self.root

        for token in tokens:
            if token not in current_node.children:
                return False
            else:
                current_node = current_node.children[token]

        return True if current_node.is_leaf_node() else False

    def remove(self, item):
        '''
        Case 1: Item is not in trie, do nothing
        Case 2: Item is not a part of any other prefix -> remove all
        Case 3: Item is in trie and has a smaller prefix within it, delete up until that prefix
        Case 4: Item is a prefix of another key in trie, unmark item's leaf
        '''
        if self.is_member(item) is False: # case 1
            return

        keys = SimpleStack()
        item = item.lower()
        tokens = list(item)
        current_node = self.root

        # get all the nodes
        for token in tokens:
            keys.push(current_node)
            current_node = current_node.children[token]

        # unmark the last node
        current_node.is_leaf = False
        last_key = current_node
        if not self._deletable(last_key): # case 4
            return

        # remove nodes marked for deletion
        while not keys.is_empty(): # case 2
            current_key = keys.pop()
            del current_key.children[last_key.key]
            if self._deletable(current_key):
                last_key = current_key
            else: # reached case 3
                return
        return

    def _deletable(self, node):
        return True if not node.is_leaf_node() and not node.has_children() \
            else False

    def remove_recursive(self, item):
        return

    def _remove_recursive_helper(self, node, item, level):
        return

    def __str__(self):
        '''
        Lists of lists trie string representation
        '''
        return str(self.__str_helper__(self.root))

    def __str_helper__(self, node):
        '''
        Recursive helper
        '''
        if node is None:
            return []

        node_list = [node.key]

        if len(node.children) == 0:
            return node_list
        else:
            node_list = [node.key]
            for child in node.children.values():
                node_list.append(self.__str_helper__(child))
            return node_list

class TrieNode:
    def __init__(self, key):
        self.key = key
        self.children = {}
        self.is_leaf = False

    def is_leaf_node(self):
        return self.is_leaf

    def has_children(self):
        return True if len(self.children) > 0 else False

    def __str__(self):
        return "TrieNode with key: " + self.key

t = Trie()
t.add("a")
t.add("answer")
t.add("any")
t.add("bye")
t.add("by")
t.add("their")
t.add("there")
t.add("the")
