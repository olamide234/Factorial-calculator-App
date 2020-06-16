import math

print('Welcome to the Factorial Calculator App')
num = int(input('What number would you like to compute factorial of? '))
print(str(num) + '! = ', end=' ')
for i in range(1, num):
    print(str(i), end='*')
print(str(num))

fact= math.factorial(num)
print('\nHere is the result from the math library: ')
print('The factorial of ' + str(num) + ' is ' + str(fact) + '!')

fact=1
for i in range(1, num+1):
    fact= fact*i
print('\nHere is the result from my own algorithm: ')
print('The factorial of ' + str(num) + ' is ' + str(fact) + '!')