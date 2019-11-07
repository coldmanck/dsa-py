count = 0

def hanoi(n):
	global count
	_hanoi(n, 'a', 'c', 'b')
	print(f'Total steps = {count}')
	count = 0

def _hanoi(n, start, end, aux):
	global count
	count += 1
	if n == 1:
		print(f'Putting {start} to {end}')
	else:
		_hanoi(n - 1, start, aux, end)
		print(f'Putting {start} to {end}')
		_hanoi(n - 1, aux, end, start)
