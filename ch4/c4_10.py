def compute_int_of_log(n):
	return _compute_int_of_log(n, 0)

def _compute_int_of_log(n, val):
	if n < 2:
		return val
	else:
		return _compute_int_of_log(n/2, val + 1)
