class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        bSum = 0  
        i=0
        for i in range(B):
            bSum +=A[i]
        j=-1
        i = B-1
        maxSum=bSum #can't initiate maxSum with 0 coz it would fail on comparision with -ve bSum
        while 0<=i<B:
            bSum=bSum - A[i] + A[j] #subtract last elem of front sum and add 1 elem from back sum
            if bSum>maxSum:
                maxSum=bSum
            i-=1
            j-=1
        return maxSum