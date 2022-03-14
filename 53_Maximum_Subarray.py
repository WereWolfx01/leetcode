class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        prevMax = float('-inf')
        cur = float('-inf')
        
        if(len(nums) == 1):
            return nums[-1]
        
        
        for num in nums:
            
            cur = max(cur+num, num)
            prevMax = max(cur, prevMax)
            
    
        return prevMax
