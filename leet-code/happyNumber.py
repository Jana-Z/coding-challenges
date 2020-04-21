class Solution(object):
    result = []
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.results = [n]
        return self.checkHappy(n)
        
    def checkHappy(self, n):
        arr = [int(d) for d in str(n)]
        result = 0
        for number in arr:
            result = result + number**2
        # print(self.results.append(result))
        if result == 1:
            return True
        elif result in self.results:
            return False
        else:
            self.results.append(result)
            return self.checkHappy(result)
