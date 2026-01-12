class Solution:
    def getMinMax(self, arr):
        minEl = 1000000001
        maxEl = -1000000001
        for i in arr:
            if i > maxEl:
                maxEl = i
            if i < minEl:
                minEl = i

        return [minEl, maxEl]
