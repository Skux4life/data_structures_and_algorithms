class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.value = val
        self.leftChild = left
        self.rightChild = right

def search(searchValue, node):
        #Base case if the node is non-existent or we've found what we're looking for
        if node is None or node.value == searchValue:
            return node

        # If the value is less than the current node, perform search on the left child
        elif searchValue < node.value:
            return search(searchValue, node.leftChild)

        # If the value is greater than the current node, perform search on the right child
        else:
            return search(searchValue, node.rightChild)

def insert(value, node):
    if value < node.value:

        # If the left child does not exist, we want to add it
        if node.leftChild is None:
            node.leftChild = TreeNode(value)
        else:
            insert(value, node.leftChild)
    
    elif value > node.value:
        # If the right child does not exist we want to add it
        if node.rightChild is None:
            node.rightChild = TreeNode(value)
        else:
            insert(value, node.rightChild)

def delete(valueToDelete, node):
    # The base is when we've hit the bottom of the tree and the parent node has no children.
    if node is None:
        return None
    
    # If the value we're deleting is less or greater than the current node we set the respective
    # left or right child to be the return value of a recursive call of this method on the current
    # node's left or right subtree.
    elif valueToDelete < node.value:
        node.leftChild = delete(valueToDelete, node.leftChild)
        return node
    elif valueToDelete > node.value:
        node.rightChild = delete(valueToDelete, node.rightChild)
        return node
    elif valueToDelete == node.value:
        # If current node has no left child, we delete it by returning its right child (and subtree if it exists)
        # to be it's parents new subtree
        if node.leftChild is None:
            return node.rightChild

        # if the current node has no left OR right child, this ends up being None as per the first line of code
        elif node.rightChild is None:
            return node.leftChild

        # If the current node has 2 children, we delete the current node by calling the lift function below
        # which changes the current node's value to the value of its successor node
        else:
            node.rightChild = lift(node.rightChild, node)
            return node

def lift(node, nodeToDelete):
    # If the current node of this function has a left child, we reucrsivley call this function
    # to continue down the left subtree to find the successor node
    if node.leftChild:
        node.leftChild = lift(node.leftChild, nodeToDelete)
        return node
    
    # If the current node has no left child, that means the current node of this function is the successor node
    # we take its value and make it the new value of the node that we're deleting
    else:
        nodeToDelete.value = node.value
        # We return the successor node's right child to be now used as its parents left child
        return node.rightChild