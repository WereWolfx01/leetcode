class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visited = []
        
        for num in nums:
            if(num in visited):
                return True
            
            else:
                visited.append(num)
        
        return False
