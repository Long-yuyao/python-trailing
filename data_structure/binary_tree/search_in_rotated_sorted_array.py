# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: list, target: int) -> int:
        l = len(nums)
        for i in range(int(l / 2)+1):
            if target == nums[i]:
                return i
            if target == nums[-1 - i]:
                return l - 1 - i
            if nums[-1 - i] < target < nums[i]:
                return -1
        return -1


print(Solution().search([1], 1))
