class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        : Solution 1: bruteforce 
        : O(n^2)
        n = len(nums)

        for i in range(n + 1):
            if i not in nums:
                return i
        """

        """
        : Solution 2: sum
        : O(1) :

        """
        n = len(nums)
        # Antatt sum fra tallene 0 til n
        exp_sum = n * (n + 1) // 2
        # Faktisk sum av elementene i arry
        act_sum = sum(nums)

        # Returnerer missing number
        return exp_sum - act_sum
        

