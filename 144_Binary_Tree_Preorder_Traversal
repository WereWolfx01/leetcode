# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
#        visited = []
#        
#        
#        
#        self.preorder(root, visited)
#        
#        return visited
#    
#    def preorder(self, root, visited):
#        if root == None:
#            return
#        
#       else:
#            visited.append(root.val)
#            self.preorder(root.left, visited)
#            self.preorder(root.right, visited)

        visited = []
        stack = [root]
        
        if root == None:
            return visited
        
        while stack:
            node = stack.pop()
            visited.append(node.val)
            if(node.right):
                stack.append(node.right)
            if(node.left):
                stack.append(node.left)
                
        return visited
        
    
