from collections import deque

def tree_by_levels(node):
    if node is None:
        return []
    stack = deque([node])
    output = deque([])
    while stack:
        current = stack.popleft()
        output.append(current.value)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    result = []
    for el in output:
        result.append(el)
    return result
