class Solution:
    def twoSum(self, arr, target):
        keymap = {}
        for i in arr:
            if target-i in keymap.keys():
                return True
            keymap[i]=1
        return False