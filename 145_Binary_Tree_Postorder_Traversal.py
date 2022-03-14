# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
#        visited = []
#        
#        if root == None:
#            return visited
#        
#        else:
#            self.postorder(root, visited)
#            return visited
#            
#            
#    def postorder(self, root, visited):
#        if root == None:
#            return
#        
#        else:
#            self.postorder(root.left, visited)
#            self.postorder(root.right, visited)
#            visited.append(root.val)
#            
#        return


        visited = []
        stack = [root]
        
        if(root == None):
            return visited
        
        while stack:
            node = stack.pop()
            
            if(node.left):
                stack.append(node.left)
            if(node.right):
                stack.append(node.right)
            visited.append(node.val)
            
        return visited[::-1]
