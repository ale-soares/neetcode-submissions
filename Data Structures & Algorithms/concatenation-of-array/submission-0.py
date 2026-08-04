class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        original_length = len(nums)
        ans = [0] * 2 * original_length

        for i in range(original_length):
            ans[i] = nums[i]
            ans[i + original_length] = nums[i]

        return ans

            