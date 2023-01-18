# Написать программу, предлагающую пользователю записывать данные о зданиях. 
# Каждое здание имеет: кол-во этажей, высоту, ширину, название. 
# Первые три свойства обязательно при инициализации должны быть числами, большими нуля. 
# Хранить данные о зданиях в структурированном файле. 
# Написать дополнительную программу (или написать 2 в 1 с меню выбора действий - по желанию), 
# которая читает здания из файла и выводит информацию о текущих записанных зданиях.
import json 

class NotValidBuilding(Exception):
    pass

class Buildings:

    def __init__(self, stairs, height, weight, name):
        self.stairs = stairs
        self.height = height
        self.weight = weight
        self.name = name
        if not self.is_valid():
            print('Ooohh... There is mistake')
            raise ValueError

    def is_valid(self):
        if self.stairs < 1 and not isinstance(self.stairs, int) and self.height  <= 0 and not isinstance(self.height, int) and self.weight <= 0 and not isinstance(self.weight, int):
            return False
        return True
        

slovar = {}
while True:
    build = input('If you want to build, push 1 but if you look to watch push 2: ')
    if build == '1':
        with open("data_file.json", "r") as read_file:
            slovar = json.load(read_file)
        s = input("Write stairs: ")
        h = input("Write height: ")
        w = input("Write weight: ")
        n = input("Write name: ")
        try:
            g = Buildings(int(s),int(h),int(w),n)
        except ValueError:
            print('Mistake!')
            continue

        slovar[g.name] = [g.stairs, g.height, g.weight]
        with open("data_file.json", "w") as write_file:
            json.dump(slovar, write_file)

    elif build == '2':
        with open("data_file.json", "r") as read_file:
            slovar = json.load(read_file)
            # print(slovar)
            for i in slovar:
                print('Name = {} stairs = {}, height = {}, weight = {}'.format(i, slovar[i][0], slovar[i][1], slovar[i][2]))
    else:
        print('Write correct num of programm')