class Solution(object):
    def __init__(self):
        self.zero_counter = 0
    
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
#       First Aproach: loop through array, when 0 move everything one up and zero to end
        for num in range(len(nums)):
            if nums[num] == 0 and num < len(nums) - self.zero_counter -1:
                zero_range = 1
                while nums[num + zero_range] == 0 and zero_range + num < len(nums) - 1:
                    zero_range += 1
                self.zero_counter = zero_range + self.zero_counter
                nums[num:] = nums[num + zero_range:] + [0]*zero_range
