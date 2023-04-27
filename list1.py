# list is nothing but array list or dynamic array

list1 = [12, 3, 6, 8, 2]

for elem in list1:
    print(elem)

colors = ["Red", "Black", "Blue"]

colors.append("Yellow")
colors.append("White")

for color in colors:
    print(color)


# sort() , len(colors) , colors[i]


text = 'bat ball'

print(len(text))

#replace ba with ro

replaced_text = text.replace('ba','ro')
print(replaced_text)

# find function --> it returns the index of first occurence of the string
str = "abcdfac"

substr = "xbc"

if str.find(substr) != -1:
    print("part of the string string")
else:
    print("not part of the string")


# .join() with lists

numList = ['1', '2', '3', '4']

print(' | '.join(numList))

# split function

cars = "BMW-Tesla-Range Rover"

#  split at '-'

print(cars.split("-"))


f=10
l=10
print(id(f))
print(id(l))