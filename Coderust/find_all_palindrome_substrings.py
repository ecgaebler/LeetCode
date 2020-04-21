def find_all_palindrome_substrings(string):

  def find_palindromes_from_index(s, idx):
    num_palindromes = 0
    #count odd-numbered palindromes, then even-numbered ones.
    for l_idx, r_idx in [[idx - 1, idx + 1], [idx, idx + 1]]:
      while l_idx >= 0 and r_idx < len(string):
        if s[l_idx] == s[r_idx]:
          num_palindromes += 1
          l_idx -= 1
          r_idx += 1
        else:
          break
    return num_palindromes
  
  palindromes = 0
  for i in range(len(string)):
    palindromes += find_palindromes_from_index(string, i)
  return palindromes