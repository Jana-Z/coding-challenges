class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        sell = 0
        buy = 0
        for day in range(1, len(prices)):
            if prices[day] < prices[day-1]: #prices shrunk -> buy now
                if sell > buy:
                    max_profit += prices[sell] - prices[buy]
                buy = day
            elif prices[day - 1] <= prices[day]: #prices rose -> sell now
                sell = day
                if sell == len(prices) - 1:
                    max_profit += prices[sell] - prices[buy]
        return max_profit
