class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums1 = sorted(nums)
        e = len(nums) // 2
        return nums1[e]

# Exemple d'utilisation
print(Solution().majorityElement([3,2,3])) # 3