# Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique

from typing import List
from collections import Counter

class Solution():
    def topKFrequent(self, nums : List[int] , k : int) -> List[int]:

        sorted_nums = sorted(nums)
        frequent = {}

        c = Counter(sorted_nums).most_common(k)
        n = len(c)

        for i in range(n):
            frequent[c[i][0]] = c[i][1]

        print(frequent)
               
        return list(frequent.keys())




if __name__ == "__main__":

    sol = Solution()
    nums = [1,2]
    k = 2
    res = sol.topKFrequent(nums,k)
    print(res)