my_dict = {'User': 123154435435, 'Admin': 321534223, 'Moder': 312312312}
print(my_dict)
print(my_dict.get('Admin'))
print(my_dict.get('Aleks'))
my_dict['Cap'] = 532432623
my_dict['Gamer'] = 345345362623
print(my_dict)
x = my_dict.pop('Moder')
print(my_dict, x)

my_set = {1, 5, 7, 3, 3, 'hello', True}
print(my_set)
my_set.add('haha')
my_set.add(12)
print(my_set)
my_set.remove(3)
print(my_set)