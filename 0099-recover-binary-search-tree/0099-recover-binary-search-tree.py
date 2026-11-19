# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root):
        nums = []
        def inorder(node):
            if node == None:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        inorder(root)
        nums.sort()
        def update(node):
            if node == None:
                return
            update(node.left)
            node.val = nums.pop(0)
            update(node.right)
        update(root)

        