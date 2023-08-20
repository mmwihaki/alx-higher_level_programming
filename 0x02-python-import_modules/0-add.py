#!/usr/bin/python3
def main():
	a = 1
	b = 2

	def add(a, b):
		return a + b
	
	result = add(a, b)
	print("{} = {} = {}".format(a, b, result))

if __name__ == "__main__":
	main()
