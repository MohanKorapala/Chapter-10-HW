class Person:

    def __init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    def print_person(self):
        print(self.__name)
        print(self.__address)
        print(self.__telephone)

class Customer(Person):

    def __init__(self, name, address, telephone,number,boolean):
        Person.__init__(self, name, address, telephone)
        self.__number = number
        self.__boolean = boolean

    def print_person(self):
        print(self.__name)
        print(self.__address)
        print(self.__telephone)
        print(self.__number)
        print(self.__boolean)