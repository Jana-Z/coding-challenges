class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#       using extra memory
        seen = []
        for number in nums:
            if number not in seen:
                seen.append(number)
            else:
                seen.remove(number)
        return seen[0]
