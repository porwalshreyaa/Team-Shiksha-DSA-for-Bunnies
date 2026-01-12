class Solution:
    def minAnd2ndMin(self, arr):
        mini = 100000
        s_min = 100000
        for i in arr:
            if i < mini:
                s_min = mini
                mini = i
            elif mini < i < s_min:
                s_min = i
        if s_min <= mini:
            return -1
        return [mini, s_min]
