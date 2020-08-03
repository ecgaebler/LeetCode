def index_equals_value_search(arr):
  """ returns first index in arr that matches the value at that index, or -1 if impossible """
  if arr[0] > 0:
    #because it's sorted and values are distinct ints, the index can never catch up
    return -1 

  l, r = 0, len(arr) - 1
  while l + 1 < r:
    mid = l + (r - l) // 2
    if mid > arr[mid]:
      l = mid
    else:
      r = mid
      
  if l == arr[l]:
    return l
  elif r == arr[r]:
    return r
  else:
    return -1
