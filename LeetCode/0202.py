class Solution:
    def isHappy(self, n: int) -> bool:
        
        def nextNum(num):
            """ returns the sum of the squares of the digits in num """
            result = 0
            while num > 0:
                result += (num % 10) ** 2
                num = num // 10
            return result
        
        tortoise, hare = n, nextNum(n)
        while tortoise != hare:
            tortoise = nextNum(tortoise) #advance tortoise one step
            hare = nextNum(nextNum(hare)) #advance hare two steps
            if tortoise == 1 or hare == 1:
                return True
        return hare == 1
        
                