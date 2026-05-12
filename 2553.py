class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            for k in range(0,len(nums)):
                if i == k: 
                    pass
                else:
                    if nums[k] + nums[i] == target:
                        return [k,i]
        
        
               
            

sol = Solution()
sol.twoSum([3,2,4], 6)