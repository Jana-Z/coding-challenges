class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_shift = 0
        for item in shift:
#           0 to left and 1 to right
            if item[0] == 0:
                total_shift -= item[1]
            else:
                total_shift += item[1]
        if total_shift > 0:               
            total_shift = total_shift % len(s)
            if total_shift == 0:
                return s
            return s[-total_shift:] + s[:len(s) - total_shift]
        else:
            total_shift *= -1
            total_shift = total_shift % len(s)
            if total_shift == 0:
                return s
            return s[total_shift:] + s[:total_shift]
