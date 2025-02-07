class Solution:
    def searchInsert(self, nums, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid]<target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
test_nums = [1,3,5,6]
test_target = 5

sol = Solution().searchInsert(test_nums, test_target)
print(sol)

        
