class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_list = [number ** 2 for number in nums]
        squared_list.sort()
        return squared_list
        