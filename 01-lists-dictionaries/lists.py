
my_list = [1, 2, 3, 4, 5, 6]

print(my_list)

my_list.append(7)
print(my_list)

# Find the sum of list elements
total = 0
for i in range(len(my_list)):
    total = total + my_list[i]

print("Total ", total)

# Another kind of loop
total = 0
for value in my_list:
    total += value   # total = total + value

print("Total ", total)

print(my_list.index(5))
try:
    print(my_list.index(5, 5))
except:
    print("5 not in the list")
my_list.insert(3, 100)

print(my_list)
