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
