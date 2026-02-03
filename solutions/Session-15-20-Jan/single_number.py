class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = set()
        for i in nums:
            if i in d:
                d.remove(i)
            else:
                d.add(i)
        for i in list(d):
            return i