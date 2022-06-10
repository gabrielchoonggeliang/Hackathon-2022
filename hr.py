from sys import argv
import random

script, hr = argv

data = open("user_data.txt", "r+")


def extract_data():
    # Replace with actual size
    # tpl4 = (value for key, value in dict2)
    tpl4 = ('XS', 'S', 'M', 'L', 'XL', '2XL', '3XL')
    for i in range(1, 100 + 1):
        data.write(f'banana{i} \t\t\t\t\t\t| {tpl4[random.randint(0, 6)]}')
        if i != 100:
            data.write('\n')


def name_list():
    dict2 = {}
    for i in data:
        d = data.readline()
        print(d)
        tpl2 = tuple(d.split(' '))
        if tpl2[0] == '':
            break
        else:
            dict2[tpl2[0]] = str(tpl2[1])[0:-1]
    print(f'dict2 = {dict2}')
    tpl3 = tuple(i for i in dict2 if dict2[i] == 'S')
    print(f"tuple of S: {tpl3}")
    print('finished~')


def size_in_order():
    pass


def write_to_data():
    data.truncate()
    data.write("Name\t\t\t\t\t\t\t  Size" + "\n" + "-"*50 + "\n")


write_to_data()
extract_data()

if hr == "employee":
    pass
elif hr == "HR":
    name_list()
