# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        self.nums = []
        self.i = 0

        def inorder(node):
            if node == None:
                return

            inorder(node.left)
            self.nums.append(node.val)
            inorder(node.right)

        inorder(root)

    def next(self):
        val = self.nums[self.i]
        self.i += 1
        return val

    def hasNext(self):
        return self.i < len(self.nums)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()