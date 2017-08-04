from library import BinaryTree, BinaryTreeNode, BinarySearchTree

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
