class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1:
            return nums2
        if not nums2:
            return nums1
        i=m-1
        j=n-1
        k = m+n-1

        while k>=0 and i>=0 and j>=0:
            if nums1[i]<nums2[j]:
                if nums1[k]==0:
                    nums1[k]=nums2[j]
                    j-=1
                else:
                    nums1[k],nums2[j]=nums2[j],nums1[k]
            else:
                nums1[k],nums1[i]=nums1[i],nums1[k]
                i-=1
            k-=1
        while k>=0 and j>=0:
            if nums1[k]==0:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        while k>=0 and i>=0:
            nums1[k],nums1[i]=nums1[i],nums1[k]
            i-=1
            k-=1
        # return nums1