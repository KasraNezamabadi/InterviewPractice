my_dict = {}
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_list = [('a', 1), ('b', 2)]
my_dict2 = dict(my_list)

target_key = 'a'
target_value = 4

if target_value in my_dict.values():
    print(target_value)
else:
    print('Value Not Found')

poped_value = my_dict.pop('a')
my_dict2.clear()


for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)







