class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        total = 0
        sq_total = 0
        n = len(nums)
        for i in nums:
            total +=i
            sq_total += i*i

        nsum = n*(n+1)//2
        nsqsum = n*(n+1)*((2*n) +1)//6
        xydiff = nsum-total
        xy_sqdiff = nsqsum-sq_total
        xysum = xy_sqdiff//xydiff
        y=(xysum+xydiff)//2
        return [xysum-y,y]

        # Intution
        # Sum of N natural numbers = n*(n+1)//2 = 1 + 2 + ...+ X + Y + ... + n
        # Sum of sq of N natural numbers = n*(n+1)*((2*n)+1)//6 = 1^2 + 2^2 + ... + X^2 + Y^2 + ... + n^2

        # total = 1 + 2 + ... + X + X + ... + n
        # sq_total = 1^2 + 2^2 + ... + X^2 + X^2 + ... + n^2

        # Sum of N natural - total = Y - X
        # Sum of Sq of N natural - sq_total = Y^2 - X^2

        # (Y+X)(Y-X) = (Y^2)-(X^2)
        # .
        # .
        # .
        # 2 * Y = (Y+X)+(Y-X)