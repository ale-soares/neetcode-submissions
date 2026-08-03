class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer, i = 0, 0

        while i < len(nums):
            if nums[i] != val:
                pointer += 1
                i += 1
            else:
                nums.pop(i)
        
        return pointer
        