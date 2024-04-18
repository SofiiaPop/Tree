def tree_by_levels(node):
    if node is None:
        return []
    stack = [node]
    output = []
    while stack:
        current = stack.pop(0)
        output.append(current.value)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return output
