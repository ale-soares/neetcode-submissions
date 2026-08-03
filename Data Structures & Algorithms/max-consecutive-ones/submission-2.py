class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # consecutives = []
        consecutive = 0
        max_consec = 0

        for n in nums:
            if n == 1:
                consecutive += 1
                
                if consecutive > max_consec:
                    max_consec = consecutive
            else:
                consecutive = 0
            
        return max_consec

        