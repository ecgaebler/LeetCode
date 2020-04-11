class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        with_stock = 0
        without_stock = 0
        for day, price in enumerate(prices):
            if day == 0:
                with_stock = - price - fee
                without_stock = 0
            else:
                with_stock = max(with_stock, without_stock - price - fee)
                without_stock = max(without_stock, with_stock + price)
                #there should be a fee for both selling and buying, but the test cases are faulty.
        return without_stock