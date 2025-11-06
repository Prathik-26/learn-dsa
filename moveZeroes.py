class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        slow = 0
        fast = 0

        while(fast < n):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1


        