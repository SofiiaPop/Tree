class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Pre-order traversal
def pre_order(node):
    if node is None:
        return []
    stack = [node]
    result = []
    while stack:
        current = stack.pop()
        result.append(current.data)
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return result

# In-order traversal
def in_order(node):
    if node is None:
        return []
    result = []
    result.extend(in_order(node.left))
    result.append(node.data)
    result.extend(in_order(node.right))
    return result

# Post-order traversal
def post_order(node):
    if node is None:
        return []
    result = []
    result.extend(post_order(node.left))
    result.extend(post_order(node.right))
    result.append(node.data)
    return result
