# Fibonacci Sequence generator
# the user enters a number 
# and generates the fibonacci sequence 
# until reach that number of length or 
# that number appears

def fibonacciSequence(n):
	'''
	Generates a fibonacci sequence
	with the  size of n
	'''
	assert n > 0

	series = [1]

	while len(series) < n:
		if n == 1:
			series.append(1)
		else:
			series.append(series[-1] + series[-2])

	for num in range(len(series)):
		series[num] = str(series[num])

	return ', '.join(series)


def main():
	n = int(input('Enter a number: '))
	print(fibonacciSequence(n))


if __name__ == '__ main__':
	main()