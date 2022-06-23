from Product import Product
from os.path import exists
import sys
class Collection:
    def __init__(self, file_name):
        self.jewss = []
        self.file_name = file_name

    def __str__(self):
        all_jewss = ""
        for item in self.jewss:
            all_jewss += str(item) + "\n"
        return all_jewss

    def read(self):
        if exists(self.file_name):
            file = open(self.file_name, 'r')
            for i, line in enumerate(file):
                dani = line.split()
                jew = Product(*dani)
                #jew = Product(*dani)
                self.jewss.append(jew)
            self.change_file()
            file.close()
            return self
        else:
            print(f'{self.file_name} does not exists')
            sys.exit()

    def change_file(self):
        file = open(self.file_name, 'w')
        for item in self.jewss:
            file.write(str(item)+"\n")
        return self

    def add(self):
        file = open(self.file_name, 'a')
        new_jew = Product()
        new_jew.input()
        self.jewss.append(new_jew)
        file.write("\n"+str(new_jew))
        return self

    def remove(self, id):
        for i in range(len(self.jewss)):
            if str(self.jewss[i].get_id()) == str(id):
                self.jewss.pop(i)
                break
        self.change_file()

    def search(self, x):
        flag = False
        for i in self.jewss:
            if i.is_found(x):
                print(i)
                flag = True
        if flag == False:
            print ("there isn't any result")

    def replace(self):
        new_jew = Product()
        new_jew.input()
        for item in self.jewss:
            if item.is_found(new_jew.get_id()):
                self.jewss.insert(self.jewss.index(item), new_jew)
                self.jewss.remove(item)
                break
        self.change_file()
        return self

    def sort(self, parameter):
        parameters = self.jewss[0].__dict__
        parameter = parameter.replace("get_", "")
        if parameter in parameters:
            self.jewss.sort(key=lambda jew_: getattr(jew_, parameter))
        else:
            print('Wrong field')
            return
        for item in self.jewss:
            self.change_file()
            print(item)
        return


def read_mistakes(path_to_file):
    file = open(path_to_file,'r')
    print(file.read())
    file.close()
    return