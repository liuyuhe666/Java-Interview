import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def select(nums, k):
            pivot = random.choice(nums)
            big, equal, small = [], [], []
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)
            if k <= len(big):
                return select(big, k)
            if len(nums) - len(small) < k:
                return select(small, k - len(nums) + len(small))
            return pivot
        return select(nums, k)
