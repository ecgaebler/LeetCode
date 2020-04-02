class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        day, have_stock, profit,  = 0, False, 0
        last_day = len(prices) - 1
        max_profit = 0
        calculated = {} #transaction format is {(day, have_stock): max_gain} 
        stack = [(day, have_stock, profit)]
        while stack:
            day, have_stock, profit = stack[-1]
            if (day, have_stock) in calculated: #check if already calculated
                profit = profit + calculated[(day, have_stock)]
                max_profit = max(max_profit, profit)
                stack.pop() #remove from stack, now that final gain was calculated
            else:
                if day == last_day:
                    if have_stock: 
                        profit = profit + prices[day] #sell stock
                    calculated[(day, have_stock)] = profit #record max gain
                else:
                    #sell stock
                    if have_stock:
                        sell_stock = (day + 1, False, profit + prices[day])
                        stack.append(sell_stock)
                    #don't sell or buy
                    no_action = (day + 1, have_stock, profit)
                    stack.append(no_action)
                    #buy stock if possible
                    if not have_stock:
                        buy_stock = (day + 1, True, profit - (prices[day] + fee))
                        stack.append(buy_stock)
        return max_profit
                    
                    