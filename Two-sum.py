class Solution:
    def twoSum(self, nums, target: int):
        output=[]
        for i in range(len(nums)):
            
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    output.append(j)
                    output.append(i)
                    return output