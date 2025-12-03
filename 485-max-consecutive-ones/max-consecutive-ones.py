# Max 1 etter hverandre
# Finn alle 1i arreyet 
# max_teller = 0
# teller = 0
# Gå igjennom arrayet 
# For i in nums: /
# sjekk om nums i = 1
# Hvis ja teller += 1
# maxTeller = max()
# Hvis i = 0:
#   teller = 0
# 
# return teller 

    

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxTeller = 0
        teller = 0

        for i in nums:
            if i == 1:
                teller += 1
                maxTeller = max(maxTeller, teller)
            else:
                teller = 0
        
        return maxTeller