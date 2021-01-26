def containsDuplicate(nums):
    values = set()
    for num in nums:
        if num in values:
            return True
        values.add(num)
    return False
