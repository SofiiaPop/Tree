class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            min_right = root.right
            while min_right.left:
                min_right = min_right.left
            root.val = min_right.val
            root.right = self.deleteNode(root.right, min_right.val)

        return root
