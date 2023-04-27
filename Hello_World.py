print("Hellow World")

#variables
a=10

b = -5

c = 7.8


print(a+b)


print(type(c))

a = 9
b = 2

#divison
print(a/b)

# Floor divison
print(a//b)

#Modulo
print(a%b)

#power ** 2**4
print(2**4)

sum = 282+138+126

print(sum)

print(sum/3)

# if else condition

x = 10
if x%2 == 0:
    print("Even")
    print("Do Something")
else:
    print("Odd")

print("hhh")

number = 9

if number > 0:
    print("positive number")
elif number < 0:    #else if == elif
    print("negative number")
else:
    print("zero")


# while loop

i = 1

while i <= 5 :
    print(i)
    i+=1 # i++ does not work in python

# for loop ..it will not include 10 in the below case

for i in range(5) : # 0---9
    print(i)

for i in range(1,5) : # 1 2 3 4
    print(i)

# to increament i by 2 like i+=2

for i in range(1,5 , 2):
    print(i)


# input is same Scanner in java.. input in python is always a string

num1 = input("Enter first number ")

num2 = input("Enter second number ")

sum = int(num1) + int(num2)

print(sum)