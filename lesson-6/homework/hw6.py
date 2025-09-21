def insert_underscores(txt):
    vowels = "aeiou"
    i = 2
    while i < len(txt) - 1:
        if txt[i] not in vowels and txt[i + 1] != "_":
            txt = txt[:i+1] + "_" + txt[i+1:]
            i += 4   # move 4 steps since we inserted an underscore
        else:
            i += 1   # shift placement if vowel or already has underscore
    return txt

print(insert_underscores("hello"))   # he_ll_o
print(insert_underscores("beautiful"))  # bea_ut_if_ul



n = int(input("Enter a number: "))

for i in range(n):
    print(i ** 2)

    #integer squares


cnt = 1
while cnt <= 10:
    print(cnt)
    cnt += 1
    #loop based


#Sum of numbers
n = 11
total = 0 
for i in range (1, n):
    total+=i

    print ("Sum =" , total)


#Multiplication table
n = int(input("Enter a number: "))
i == 1
while i <= 10:
    print (f"{n} * {i} = {n * i} ")
    i+=1


#Count digits
x = 75869
print("Numbers of digits:", len(str(x))) 


#Reverse list
for i in range (len(list1)-1, -1, 1,-1):
    print (list1[i])


#Fibonacci
n = 10
a, b = 0, 1

print("Fibonacci sequence:")

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

#Uncommon elements of lists
def uncommon_elements(list1, list2):
    return list(set(list1) ^ set(list2))   # symmetric difference
