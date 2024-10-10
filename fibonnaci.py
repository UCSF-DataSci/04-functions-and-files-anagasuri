#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""

import argparse

def fibonacci(limit):
	x = 0
	y = 1

	FibList = []

	while x < limit:
		FibList.append(x)
		
		temp = x + y # computes fibonacci number, temp hold fibonnaci number 
		x = y # updates value of x to the value of y, the second to last fibonnaci number 
		y = temp # now y is the last fibonnaci number 
	
	return FibList

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description="Generate Fibonacci numbers less than 100.")
	parser.add_argument('--limit', type=int, default=100, 
                        help='Upper limit for generating Fibonacci numbers (default: 100).')
	parser.add_argument('--output_file', type=str, 
                        help='Path to the output file to save the Fibonacci numbers.')
	args = parser.parse_args()

	FinalFibonacci = fibonacci()
	print(FinalFibonacci) 

	if args.output_file:
		with open(args.output_file, 'w') as f:
			for number in FinalFibonacci:
				f.write(f"{number}\n")
		print(f"Fibonacci numbers saved to {args.output_file}.")

# run this in terminal: python3 fibonnaci.py --output_file fibonacci_numbers.txt 