import numpy as np

a = np.arange(15).reshape(3, 5)

print(a)

print("shape")
print(a.shape)

print("size")
print(a.size)

print("ndim")
print(a.ndim)

print("dtype name")
print(a.dtype.name)

print("type")
print(type(a))

## Array Creation

a = np.array([1,2,3,4])
print(a)
print("array dtype")
print(a.dtype)

b = np.array([1.2, 3.5, 6.9])
print("array dtype")
print(b.dtype)

## The type of the array can also be explicitly specified at creation time

c= np.array([[1,2],[3,4]] , dtype=complex)
print(c)

z=np.zeros((3,4),dtype=int)
print(z)

one = np.ones((2,3,4), dtype=np.int16)
print(one)

# To create sequences of numbers,
# NumPy provides the arange function which is analogous to the Python built-in range, but returns an array.
ap=np.arange(10, 30, 5)
print(ap)

ut = np.arange(0, 2, 0.3)  # it accepts float arguments
print(ut)
# function linspace that receives as an argument the number of elements that we want, instead of the step:
ls = np.linspace(0, 2, 9) # 9 numbers from 0 to 2

print(ls)


## Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result.

a = np.array([20,30,40,50])
b = np.arange(4)
print(b)

c = a - b
print("c=a-b ")
print(c)

d = b**2
print("d=b**2")
print(d)

e = a < 35
print("e = a < 35")
print(e)

f = 10 * np.sin(a)
print("f = 10 * np.sin(a)")
print(f)

#Unlike in many matrix languages, the product operator * operates elementwise in NumPy arrays.
#The matrix product can be performed using the @ operator (in python >=3.5)
# or the dot function or method:

A = np.array([[1, 1],
              [0, 1]])

B = np.array([[2, 0],
              [3, 4]])
print("elementwise product ")
P = A * B     # elementwise product
print(P)

print("matrix product using @")
P2 = A @ B     # matrix product

print(P2)

print("matrix product using dot ")
P3 = A.dot(B)  # another matrix product

print(P3)

print("Random")

rg = np.random.default_rng(1)  # create instance of default random number generator

r = rg.random((2,3))
print(r)

s = r.sum()
print(s)

print(r.min())

print(r.max())

#By default, these operations apply to the array as though it were a list of numbers,
# regardless of its shape. However, by specifying the axis parameter you can apply
# an operation along the specified axis of an array:

print("axis parameter usage 0 - column , 1 - row")
b = np.arange(12).reshape(3, 4)
print(b)

print(b.sum(axis=0))    # sum of each column

print(b.min(axis=1))    # min of each row

print(b.cumsum(axis=1))  # cumulative sum along each row
