class Solution:
    def twoSum(self, numbers,target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            csum = numbers[left] + numbers[right]
            if csum == target:
                return [left+1,right+1]
            elif csum < target:
                left += 1
            else:
                right -= 1
        return []

'''
If you are running outside leetcode, add this code to test your solution:
numbers = [2,7,11,15]
target = 9
solution = Solution()
result = solution.twoum(numbers,target)
print(result)
'''