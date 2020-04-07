class Solution:
    def countElements(self, arr: List[int]) -> int:
        import collections
        result = 0
        dictionary = collections.Counter(arr)
        for item in dictionary:
            if item + 1 in dictionary:
                result += dictionary[item]
        return result
