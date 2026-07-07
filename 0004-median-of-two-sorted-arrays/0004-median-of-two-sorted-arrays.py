class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num = nums1 + nums2
        l = len(num) 
        for j in range(l):
            for k in range(l):
                if (num[j] > num[k]):
                    aux = num[j]
                    num[j] = num[k]
                    num[k] = aux
        sum = 0
        if (l % 2 == 0):    
            sum += num[l//2 - 1] + num[(l//2)]
            return float(sum/2.0)
        return float(num[l//2])
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        