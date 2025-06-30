class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numSize=len(nums)
        for i in range(numSize) :
            for j in range(i+1,numSize) :
                if (nums[i]+nums[j])==target :
                    return i,j
              
