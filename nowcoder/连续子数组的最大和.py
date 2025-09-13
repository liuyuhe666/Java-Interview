from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型
#
class Solution:
    def FindGreatestSumOfSubArray(self, array: List[int]) -> int:
        # write code here
        n = len(array)
        if n <= 0:
            return 0
        ans, total = array[0], 0
        for i in range(n):
            if total < 0:
                total = array[i]
            else:
                total += array[i]
            if total > ans:
                ans = total
        return ans
