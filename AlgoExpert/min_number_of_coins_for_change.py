def minNumberOfCoinsForChange(n, denoms):
    min_coins = [float("inf") for _ in range(n + 1)]
	min_coins[0] = 0
	for denom in denoms:
		for target in range(n + 1):
			if denom <= target:
				min_coins[target] = min(min_coins[target], 1 + min_coins[target - denom])
	if min_coins[n] == float("inf"):
		return -1
	return min_coins[n]
