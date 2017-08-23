from graph import Vertex

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

    def is_member(self, item):
        return

    def remove(self, item):
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

    def is_leaf(self):
        return self.is_leaf

    def __str__(self):
        return "TrieNode with key: " + self.key

