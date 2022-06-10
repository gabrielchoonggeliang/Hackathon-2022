import random

a = open('hr_data.txt', 'r+')
a.truncate()
tpl4 = ('XS', 'S', 'M', 'L', 'XL', '2XL', '3XL')
for i in range(1, 100+1):
    a.write(f'banana{i} {tpl4[random.randint(0, 6)]}')
    if i != 100:
        a.write('\n')
dict2 = {}
a.seek(0)
for i in a:
    d = a.readline()
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
a.close()
