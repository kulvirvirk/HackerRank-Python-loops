# Task
# Read an integer N. For all non-negative integers i < N, print i**2 .See the sample for details.

#Input Format
# The first and only line contains the integer, N.

# constraints: 
# 1 <= N <=20

# Output Format: 
# Print N lines, one corresponding to each i 

# Link - https://www.hackerrank.com/challenges/python-loops/problem 

n = int(input('enter N:'))

if n >= 1 and n <= 20:
  for i in range(0, n):
    print(i**2)
else: 
  print('Invalid input, plz re-run the program!')
