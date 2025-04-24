class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid  # Found it
            elif nums[mid] < target:
                low = mid + 1  # Search right
            else:
                high = mid - 1  # Search left
        
        return low  # Where it should be inserted
