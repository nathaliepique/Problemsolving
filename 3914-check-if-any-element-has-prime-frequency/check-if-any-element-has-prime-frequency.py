class Solution(object):
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Sjekker om n er primtall
        def er_prim(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        n = len(nums)

        # Bruteforce: tell frekvens for hvert element
        for i in range(n):
            count = 0

            for j in range(n):
                if nums[j] == nums[i]:
                    count += 1

            # Sjekk om frekvensen er primtall
            if er_prim(count):
                return True

        return False
            


                