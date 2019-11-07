'''
Check if the parameter string has delimiters matched.
parameter: s -> str
return: bool
'''

from ArrayStack import ArrayStack

def is_matched(s):
	left = '([{'
	right = ')]}'
	stack = ArrayStack()

	for c in s:
		if c in left:
			stack.push(c)
		elif c in right:
			if stack.is_empty():
				return False
			elif left.index(stack.pop()) != right.index(c):
				return False

	return stack.is_empty()
