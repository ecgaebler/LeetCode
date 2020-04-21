def can_segment_string(s, dictionary):
  calculated = {} #stores whether it is possible to segment starting at a given index

  def can_use(s, index, word):
    """ Returns true if given word matches string s, starting at given index. """
    if len(word) > len(s) - index:
      return False
    for i in range(len(word)):
      if s[index + i] != word[i]:
        return False
    return True

  def can_segment(s, index, d, memo):
    """ Returns True if s[index:] can be segmented using dictionary 'd' and memoization 'memo' """
    if index in memo:
      return memo[index]
    if len(s) - index == 0:
      return True
    for word in d:
      if can_use(s, index, word): #s starts with word
        #print("can use string:",word) #DEBUG
        if can_segment(s, index + len(word), dictionary, memo): #can segment string after subtracting word
          memo[index] = True
          #print("can segment", s[index+len(word):]) #DEBUG
          return True
        else:
          memo[index + len(word)] = False
    #Reaching this point means no valid segmentation was found
    memo[index] = False
    return False 
  
  return can_segment(s, 0, dictionary, calculated)
