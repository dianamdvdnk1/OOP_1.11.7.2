
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
        if self.stairs < 1 or not isinstance(self.stairs, int) or self.height  <= 1 or not isinstance(self.height, int) or self.weight <= 1 or not isinstance(self.weight, int):
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
    
    elif build == 'q':
        print('Bye')
        break
    else:
        print('Write correct num of programm')