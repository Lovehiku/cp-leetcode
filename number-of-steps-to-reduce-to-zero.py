class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
            count += 1
        return count 
sol = Solution()
print(sol.numberOfSteps(14)) 
print(sol.numberOfSteps(8))
