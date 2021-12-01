from Linked_list import LinkedList
from iterator_generator import *

def inputing_size():
    chek = False
    size = 0
    while(chek == False):
        try:
            size = int(input("Enter a list  size "))
            if size > 0:
                chek = True
            else:
                chek = False
                print('Size should be > 0')
        except ValueError:
            print('You should have entered an int value. Try again')
    return size

def filling_list(size):
    result = []
    for i in range(size):
        element = int(input('Enter an element '))
        result.append(element)
    return result

def menu():
    my_list = LinkedList()
    while True:
        try:
            print(
                "1 - create list,inputing elements \n2 - create randome list in your diapazone \n3- add el at certain position \n4- del el from certain position \n5- show list\n6 - do method\n7 - generator\n8 - iterator\n0 - exit the program ")
            Choose = input()
            if (Choose == '1'):
                size = inputing_size()
                list = filling_list(size)
                for i in range(size):
                    my_list.apppend(list[i])
                my_list.show()
            elif (Choose == '2'):
                size = inputing_size()
                start = int(input('Enter from which value should we start '))
                end = int(input('Enter a value to which we should generate '))
                my_list.generate_list(size, start, end)
                my_list.show()
            elif (Choose == '3'):
                input_ = int(input('Enter what should be inserted into a list '))
                position = int(input('Enter a position on which a value should be inserted '))
                #print(my_list.insert(position, input_))
                my_list.insert(position, input_)
            elif (Choose == '4'):
                position = int(input('Enter a position on which a value should be deleted '))
                my_list.remove(position)
            elif (Choose == '5'):
                my_list.show()
            elif (Choose == '6'):
                my_list.method()
            elif (Choose == '7'):
                size = inputing_size()
                start = int(input('Enter from which value should we start '))
                end = int(input('Enter a value to which we should generate '))
                my_list.uusing_generator_or_iterator(generator(size, start, end))
                my_list.show()
            elif (Choose == '8'):
                size = inputing_size()
                start = int(input('Enter from which value should we start '))
                end = int(input('Enter a value to which we should generate '))
                my_list.using_generator_or_iterator(Iterator(size, start, end))
                my_list.show()

            elif (Choose == '0'):
                print('End of program')
                break
            else:
                print('Unknown option was entered. Try again')
                continue
        except ValueError:
            print('You should have entered an int value. Try again')

menu()

