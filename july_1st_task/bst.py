class BSTNode:

    def __init__(self, data):

        self.data = data

        self.left = None

        self.right = None
        
def insert(node, data):

    if node is None:
        return BSTNode(data)

    if data < node.data:
        node.left = insert(node.left, data)

    elif data > node.data:
        node.right = insert(node.right, data)

    return node

def search(node, target):

    if node is None:
        return False

    if node.data == target:
        return True

    if target < node.data:
        return search(node.left, target)

    return search(node.right, target)

def inorder(node):

    if node:

        inorder(node.left)

        print(node.data, end=" ")

        inorder(node.right)
        
root = None
root = insert(root, 5)
root = insert(root, 3)
root = insert(root, 7)
inorder(root)
search_result = search(root, 3)
print("\nSearch result for 3:", search_result)