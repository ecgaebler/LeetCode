def numberOfWaysToMakeChange(n, denoms):
	ways = [0 for i in range(n + 1)]
	ways[0] = 1
	for denom in denoms:
		for target in range(1, n + 1):
			if denom <= target:
				ways[target] += ways[target - denom]
	return ways[n]
