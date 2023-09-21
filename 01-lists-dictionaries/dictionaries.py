
my_dict = {}

my_dict['a'] = 1000
my_dict['b'] = 500

for key in my_dict:
    print(key, end=': ')
    print(my_dict[key])

if 'a' in my_dict:
    print("a exists")
else:
    print("a is not here")

my_list = ["burger", "pizza", "falafel", "pizza", "tacos", "burger", "pizza"]

# How many of each food were sold
items = {}
for food in my_list:
    if food in items:
        items[food] += 1
    else:
        items[food] = 1

for key in items:
    print(key, ":", items[key])

