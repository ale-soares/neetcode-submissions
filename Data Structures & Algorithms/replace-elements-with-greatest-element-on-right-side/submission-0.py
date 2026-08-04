class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            arr[i] = 0
            arr[i] = max(arr[i:])
        
        arr[-1] = -1
        return arr


        