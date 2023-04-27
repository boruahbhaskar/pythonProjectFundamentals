## sum of digits of a number say 1234 = 10


def find_sum_of_digit(number): # (number: int) we can add type of the parameter or str
    sum = 0

    while number > 0 :
        sum += number%10
        number = number // 10

    return sum


def find_sum(*numbers) -> int : # *numbers means list of numbers in the input
  sum = 0
  for num in numbers:
      sum += num

  print(sum)

find_sum(1,2,3,4,5)

print(find_sum_of_digit(1234))

# function

def add(a,b): # argument
    return a + b

print(add(4,8))

sum = add(12, 9) # parameter

print(sum)