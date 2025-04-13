# Loops

# While loop
num = 1
while num <= 100:
    print(num)
    num += 1


# Break in a loop
i = 1
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1


# Continue in a loop
    i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1




# For loop
name = "alexander white garrid"
for char in name:
    print(char)



# Range in loop
n = int(input("Enter a number: "))
for i in range(1, 11):
   print(i * n)


# LIST
name = ["alice", "bob", "charlie", "danny", "edam", "frank"]
print(name[0:3])

# List Methods
list = [1,2,3,4,5]
list.append(6) 
print(list)


list = [1,9,3,7,5]
print(list.sort())
print(list)

list=["a", "b", "c", "d"]
list.reverse()
print(list)

list = [1,2,3,4,5]
list.insert(5,6)
print(list)



# Tuple
num = (1, 2, 3, 4, 1, 2)
print(num.index(2))


grade = ["C","A","B","D","A","C","A"]
print(grade.count("A"))
grade.sort()
print(grade)



# Dictionary
info = {
    "name" : "ally",
    "age" : 21,
    "hobby" : "reading"
}
print(info)

# Nested dictionary
info = {
    "name" : "ally",
    "age" : 21,
    "hobby" : "reading",
    "subjects" : {
        "physics" : 78,
        "english" : 89,
        "bio" : 85,
        "chem" : 82
    }
}
print(info["subjects"]["physics"])

# DICT Methods

print(list(info.keys()))
print(len(list(info.keys())))

print(info.values())

print(info.items())
pairs = list(info.items())
print(pairs[1])



# SETS
collection = {1, 2, 3 , 4, 5, 1}
print(collection)

# Set Methods
copies = set()
copies.add(1) # can add only one element at a time
copies.add(2)
copies.remove(1)
print(copies)
print(copies.pop())

# Frozen set
my_list = [1, 2, 3, 2, 1]
fs = frozenset(my_list)
print("Frozenset:", fs)

a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

print("Union:", a | b)           
print("Intersection:", a & b)    
print("Difference:", a - b) 