class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """ : Solution 1: brute force and very slow
            : O(n^2) time complexity
    
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
        """
         
        """ : Solution 2: Bruk av hashtabell -> dictionary i python
            : O(n) time complexity 
        """
        hashtabell = {}

        for i in range(len(nums)):
            rest = target - nums[i]

            if rest in hashtabell:
                return [hashtabell[rest], i]
        
            hashtabell[nums[i]] = i    
        