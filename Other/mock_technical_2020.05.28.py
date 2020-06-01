'''
Given a positive int n, print all jumping numbers smaller than or equal to n. A number is called a jumping number if all adjacent digits in it differ by 1. 
For example, 8987 and 4343456 are jumping numbers, but 796 and 89098 are not. All single digit numbers are considered as jumping numbers.

Example:

Input: 105
Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98, 101]
'''

def jumping_numbers(n):
    """ return the list of jumping numbers not larger than n. """
    def jumping(x, n, result):
        """ given a jumping number, create new jumping numbers by appending digits. """
        if x <= n:
            result.append(x)
        d = x%10
        if x <= n//10: #Make sure the next jumping numbers won't be too large.
            if d > 0:
                jumping(x*10+d-1, n, result)
            if d < 9:
                jumping(x*10+d+1, n, result)
                
    if n < 10:
        return [_ for _ in range(n+1)]
    result = [0] #Keep 0 outside loop so we don't try appending digits to a leading 0.
    for x in range(1, 10):
        jumping(x, n, result)
    return sorted(result)

