class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        
        if len(nums) == 0 or (len(nums) == 1 and val in nums):
            return 0
        elif val not in nums:
            return len(nums)
        
        nums.sort()
        
        for j in range(1, len(nums)):
            if nums[i] == val and nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
            
            if nums[i] != val: 
                i += 1
        
        return i