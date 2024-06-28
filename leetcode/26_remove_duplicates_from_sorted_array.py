class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
        
        

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  # Doit retourner 5   