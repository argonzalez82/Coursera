#Week 3 Practice Quiz : While Loops 


#QUESTION 2:

def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor = factor + 1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT


#QUESTION 3:

def is_power_of_two(n):
  # Check if n == 0, if True exit as False to prevent endless loop.
  if n == 0:
    return False
  # Check if the number can be divided by two without a remainder  
  while n % 2 == 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False


#QUESTIONS 4:


def sum_divisors(n):
  # Return the sum of all divisors of n, not including n
  return sum([i for i in range(1, n)
                if n % i == 0])
                
print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114


#QUESTION 5:

def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = multiplier * number 
		# What is the additional condition to exit out of the loop?
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24

#  sudo ln -sv /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/bin/subl



"""**************End of Quiz***********************"""


#Week 3 For Loop Quiz 


#QUESTION 2:
'''Fill in the blanks to make the factorial function return the factorial of n. 
Then, print the first 10 factorials (from 0 to 9) with the corresponding number. 
Remember that the factorial of a number is defined as the product of an integer and 
all integers before it. For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. 
Also recall that the factorial of zero (0!) is equal to 1.'''

def factorial(n):
    result = 1
    for x in range(0,n):
        result = x * n - 1
    return result

for n in range(0,10):
    print(n, factorial(n+1))



#QUESTION 3:
#Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.

for x in range(1,11):
  cubed = x ** 3
  print(cubed)


