def k_divider(k, arr):
	return _k_divider(k, arr, 0, len(arr) - 1)

def _k_divider(k, arr, begin, end):
	if begin >= end:
		return
	else:
		if arr[begin] > k:
			arr[begin]
