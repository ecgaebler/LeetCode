def longestPeak(array):
	longest_peak = 0
	if len(array) < 3:
		return longest_peak
	
	#find peaks
	peaks = []
	for i in range(1, len(array) - 1):
		if array[i - 1] < array[i] > array[i+1]:
			peaks.append(i)
	
	#determine size of peaks
	for peak_idx in peaks:
		peak_length = 1
		left_idx, right_idx = peak_idx, peak_idx
		
		#count left slope
		while left_idx > 0 and array[left_idx - 1] < array[left_idx]:
			peak_length += 1
			left_idx -= 1
		
		#count right slope
		while right_idx < len(array) - 1 and array[right_idx + 1] < array[right_idx]:
			peak_length += 1
			right_idx += 1
		
		if peak_length > longest_peak:
			longest_peak = peak_length
	
	return longest_peak