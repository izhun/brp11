def factorial(n):
	"""fact func"""
    if n == 0:
        return 1
    return n * factorial(n-1)
