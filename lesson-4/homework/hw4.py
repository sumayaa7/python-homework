#2
my_dict = {0: 10, 1: 20}
my_dict[1] = 20
print(my_dict)

#3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)
print(result)

#4
n = 5
squares = {}
for x in range(1, n + 1):
    squares[x] = x * x
print(squares)

#5
squares = {}
for x in range(1, 16):
    squares[x] = x * x
print(squares)

#Set Exercise
#1
my_set = {1, 2, 3}
print(my_set)

#2
my_set = {10, 20, 30}
for item in my_set:
    print(item)

#3
my_set = {1, 2}
my_set.add(3)         # add one
my_set.update([4, 5]) # add many
print(my_set)

#4
my_set = {1, 2, 3, 4}
my_set.remove(3)  # removes 3
print(my_set)

#5
my_set = {1, 2, 3}
if 2 in my_set:
    my_set.remove(2)
print(my_set)
