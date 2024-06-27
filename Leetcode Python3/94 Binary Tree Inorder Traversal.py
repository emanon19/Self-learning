# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        node = root
        while node:
            if node.left is None:
                yield node.val
                node = node.right
            else:
                tmp = node.left
                while tmp.right and tmp.right != node:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right, node = node, node.left
                else:
                    yield node.val
                    node, tmp.right = node.right, None

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = list()
        def dfs(node):
            if not node:
                return res
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            
        dfs(root)
        return res
