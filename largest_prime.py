#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

# You're on your own for this one. Good luck!
import argparse
from fibonnaci import fibonacci  # Fixed typo in module name

# Function to check if a number is prime
def primeNum(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True 

# Function to find the largest prime Fibonacci number from the given list
def largestPrime(fibList): 
    prime = [i for i in fibList if primeNum(i)]
    if prime:
        return max(prime)
    else: 
        return None 
    

if __name__ == "__main__":
    # Parse the arguments
    parser = argparse.ArgumentParser(description="Find the largest prime Fibonacci number.")
    parser.add_argument('--limit', type=int, default=100, help='Upper limit for generating Fibonacci numbers.')
    args = parser.parse_args()

    # Generate Fibonacci numbers up to the given limit
    FibList = fibonacci(args.limit)  # Make sure fibonacci() accepts a limit argument

    # Find the largest prime Fibonacci number
    largest_prime = largestPrime(FibList)
    
    if largest_prime is not None:
        print(f"Largest prime Fibonacci number less than {args.limit}: {largest_prime}")
    else:
        print(f"No prime Fibonacci numbers found under {args.limit}.")
