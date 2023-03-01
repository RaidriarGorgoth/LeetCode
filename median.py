class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1=nums1+nums2
        nums1.sort()
        median=0
        if(len(nums1)%2==0):
            mid=(len(nums1)-0)/2
            mid1=mid-1
            median=float((float(nums1[mid])+float(nums1[mid1])))/2
        else:
            mid=(len(nums1)-0)/2
            median=nums1[mid]
        return median
