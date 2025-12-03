# Vi vet n = antall plasser i nums 1n og dette blir repetert
# Vi skal split array til 2 deler
# Merge annehver tall
# Returner array arr


class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
    
        n = len(nums) // 2
        arr = []

        left = nums[:n]
        right = nums[n:]

        for i in range(len(left)):
            arr.append(left[i])
            arr.append(right[i])
    
        return arr