def hanoi(n):
	_hanoi(n, 'a', 'c', 'b')

def _hanoi(n, start, end, aux):
	if n == 1:
		print(f'Putting {start} to {end}')
	else:
		_hanoi(n - 1, start, aux, end)
		print(f'Putting {start} to {end}')
		_hanoi(n - 1, aux, end, start)
