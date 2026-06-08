class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = {}
        for num in nums:
            if num not in arr:
                arr[num] = 1
            else:
                return True 
        return False