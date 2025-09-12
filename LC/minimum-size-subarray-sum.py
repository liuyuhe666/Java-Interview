from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = n + 1
        left, right = 0, 0
        total = 0
        while right < n:
            total += nums[right]
            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        return 0 if ans == n + 1 else ans
