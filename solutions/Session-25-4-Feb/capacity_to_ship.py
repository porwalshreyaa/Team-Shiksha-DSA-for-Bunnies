import math
def calc_days_to_ship(arr:list, cap:int)->int:
    sum_of_w =0
    count_days=1
    for i in arr:
        if sum_of_w + i> cap:
            sum_of_w =0
            count_days +=1
        sum_of_w+=i
    return count_days

class Solution:
    def shipWithinDays(self, weights:list, days: int) -> int:
        max_elem=0
        sum_of_arr=0
        for i in weights:
            if i > max_elem:
                max_elem = i
            sum_of_arr +=i
        low = max_elem
        high = sum_of_arr
        possible_cap = sum_of_arr
        while low <=high:
            mid = math.ceil((low+high)/2)
            calc_days = calc_days_to_ship(weights,mid)
            if calc_days > days:
                low = mid+1
                continue
            if mid<possible_cap:
                possible_cap = mid
            high = mid-1
        return possible_cap

sol = Solution()


print(sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))
print(sol.shipWithinDays([3,2,2,4,1,4],3))
print(sol.shipWithinDays([1,2,3,1,1],4))