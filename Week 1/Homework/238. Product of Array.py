from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        l_product = 1
        for i in range(n):
            ans[i] *= l_product
            l_product *= nums[i]
        r_product = 1
        for i in range(n-1,-1,-1):
            ans[i] *= r_product
            r_product *= nums[i]
        return ans

'''
If you are running outside leetcode, add this code to test your solution:
solution = Solution()
nums = [1, 2, 3, 4]
print(solution.productExceptSelf(nums))
'''