class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            left=0
            right=len(nums)-1
            mid=(left+right)//2
            while(left<=right):
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    left+=1
                    mid+=1
                else:
                    right-=1
                    mid-=1
        else:
            return -1
    