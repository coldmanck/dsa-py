def find_min_max(arr):
	if len(arr) < 2:
		return arr[0], arr[0]
	return min_max(arr, len(arr) - 1, arr[0], arr[0])

def min_max(arr, idx, minval, maxval):
	if idx == -1:
		return minval, maxval
	else:
		if arr[idx] < minval:
			minval = arr[idx]
		if arr[idx] > maxval:
			maxval = arr[idx]
		return min_max(arr, idx - 1, minval, maxval)

# minval, maxval = find_min_max(arr)
# print('Min value: ' + minval + ', Max value: ' + maxval)
