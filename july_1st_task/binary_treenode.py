class TreeNode:

    def __init__(self, data):

        self.data = data

        self.left = None

        self.right = None
        
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

#height of the binary tree
def height(node):

    if node is None:
        return 0

    left_height = height(node.left)

    right_height = height(node.right)

    return 1 + max(left_height, right_height)

height_of_tree = height(root)
print("Height of the binary tree:", height_of_tree)

#count the number of nodes in the binary tree
def count_nodes(node):

    if node is None:
        return 0

    return 1 + count_nodes(node.left) + count_nodes(node.right)

count_of_nodes = count_nodes(root)
print("Count of nodes in the binary tree:", count_of_nodes)

#count the number of leaf nodes in the binary tree
def count_leaves(node):

    if node is None:
        return 0

    if node.left is None and node.right is None:
        return 1

    return count_leaves(node.left) + count_leaves(node.right)

count_of_leaves = count_leaves(root)
print("Count of leaf nodes in the binary tree:", count_of_leaves)

#inorder traversal of the binary tree
def inorder(node, result=None):

    if result is None:
        result = []

    if node:

        inorder(node.left, result)

        result.append(node.data)

        inorder(node.right, result)

    return result

inorder_result = inorder(root)
print("Inorder traversal of the binary tree:", inorder_result)

#preorder traversal of the binary tree
def preorder(node, result=None):

    if result is None:
        result = []

    if node:

        result.append(node.data)

        preorder(node.left, result)

        preorder(node.right, result)

    return result

preorder_result = preorder(root)
print("Preorder traversal of the binary tree:", preorder_result)

#postorder traversal of the binary tree
def postorder(node, result=None):

    if result is None:
        result = []

    if node:

        postorder(node.left, result)

        postorder(node.right, result)

        result.append(node.data)

    return result

postorder_result = postorder(root)
print("Postorder traversal of the binary tree:", postorder_result)

#level order traversal of the binary tree
from collections import deque

def level_order(root):

    if root is None:
        return []

    queue = deque([root])

    result = []

    while queue:

        node = queue.popleft()

        result.append(node.data)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result

level_order_result = level_order(root)
print("Level order traversal of the binary tree:", level_order_result)