class Solution(object):
    def singleNumber(self, nums):
        nums.sort()

        if len(nums) == 1:
            return nums[0]

        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                return nums[i]
            i += 2

        return nums[-1]
    
    """
    Problemet kan løses med XOR sammenligning for å oppnå O(n) og konstant plassav O(1)
    To Do:
    """
