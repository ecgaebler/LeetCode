
def levenshteinDistance(str1, str2):
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)
    
    #dp table for cost of converting substrings of str1 into substrings of str2
    #note that the range we use goes to len + 1, because we need a row and
    #column for empty strings
    dp = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
    #initialize first row and first column
    for i in range(len(str1) + 1):
        dp[0][i] = i
    for j in range(len(str2) + 1):
        dp[j][0] = j
    
    for j in range(1, len(str2) + 1):
        for i in range(1, len(str1) + 1):
            #note: I use i - 1 and j - 1 because the table is 1 wider and taller
            #than the string lengths, to account for the empty substrings.
            if str1[i - 1] == str2[j - 1]: 
                dp[j][i] = dp[j - 1][i - 1]
            else:
                add_cost = dp[j][i - 1] + 1
                del_cost = dp[j - 1][i] + 1
                sub_cost = dp[j - 1][i - 1] + 1
                dp[j][i] = min(add_cost, del_cost, sub_cost)

    return dp[-1][-1]

'''
  "" a b c -str1(i)
"" 0 1 2 3
 y 1 1 2 3
 a 2 1 2 3
 b 3 2 1 2
 d 4 3 2 2
str2(j)

  "" a b b -str1(i)
"" 0 1 2 3
 b 1 1 1 2
 b 2 1 1 1
 a 3 2 2 2
str2(j)
'''
test0 = ("abc", "yabd")
test1 = ("abb", "bba")
tests = [test0, test1]
for str1, str2 in tests:
    print((str1, str2))
    print(levenshteinDistance(str1, str2))
