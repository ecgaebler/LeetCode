def threeNumberSum(array, targetSum):
	sorted_array = sorted(array)
	triplets = []
	for i in range(len(array) - 2):
		left = i + 1
		right = len(array) - 1
		while left < right:
			current_sum = sorted_array[i] + sorted_array[left] + sorted_array[right]
			if current_sum < targetSum:
				left += 1
			elif current_sum > targetSum:
				right -= 1
			else:
				triplets.append([sorted_array[i], sorted_array[left], sorted_array[right]])
				left += 1
				right -= 1
	return triplets