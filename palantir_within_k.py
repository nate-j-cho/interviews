def duplicates(arr, k):
	set = {}
	
	for a in xrange(len(arr)):
		current = arr[a]
		start = arr[a-k]
		
		if current in set:
			return true
		
		set[arr[current]] += 1
		set[arr[current]+1] += 1
		set[arr[current]-1] += 1
			
		if a >= k:
			del set[start]
			set[start] -= 1
			set[start+1] -= 1
			set[start-1] -= 1
		
		set[current] = current
		
	return false
	
def duplicates(arr, k, I):
	set = {}
	
	for i in xrange(len(arr)):
		if i > k:
			del set[arr[i-k-1]/I]
		if ((arr[i]/I) in set) or \
		((arr[i]/I-1) in set and set[arr[i]/I-1] - arr[i] >= -I) or \
		((arr[i]/I+1) in set and set[arr[i]/I+1] - arr[i] <= I):
			return True
		
		set[arr[i]/I] = arr[i]
	return False
