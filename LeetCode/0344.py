def reverseString(s):
    """
    Reverse a list of chars in place.
    Do not return anything.
    """
    left_idx, right_idx = 0, len(s) - 1
    while right_idx > left_idx:
        s[left_idx], s[right_idx] = s[right_idx], s[left_idx]
        left_idx += 1
        right_idx -= 1
