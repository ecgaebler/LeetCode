def threeNumberSum(array, targetSum):
	val_indexes = {}
	for idx, num in enumerate(array):
		if num not in val_indexes:
			val_indexes[num] = []
		val_indexes[num].append(idx)
		
	def two_sum_ignore(target, ignore_idx):
		pairs = set()
		for idx1, num1 in enumerate(array):
			if idx1 == ignore_idx:
				continue
			if target-num1 in val_indexes:
				for idx in val_indexes[target-num1]:
					if idx != idx1 and idx != ignore_idx:
						pairs.add(tuple(sorted([num1, target-num1])))
						break
		return pairs
		
	triples = set()
    for i0, n0 in enumerate(array):
		for pair in two_sum_ignore(targetSum - n0, i0):
			unpacked = list(pair).append(n0)
			triples.add(tuple(sorted(unpacked)))
	
	triple_list=sorted(list(triples), key=lambda x: x[0])
	result = []
	for triple in triple_list:
		result.append(triple)
	return result
		
