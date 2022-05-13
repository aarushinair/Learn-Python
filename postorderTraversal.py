class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
def printPostorder(root):
 
    if root:
 
        # First recur on left child
        printPostorder(root.left)
 
        # the recur on right child
        printPostorder(root.right)
 
        # now print the data of node
        print(root.val),
root = Node(6)
root.left = Node(7)
root.right = Node(8)
root.left.left = Node(9)
root.left.right = Node(10)
print "\nPostorder traversal of binary tree is"
printPostorder(root)
