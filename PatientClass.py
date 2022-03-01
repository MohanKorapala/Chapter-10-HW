from numpy import printoptions


class Patient:

    def __init__(self, iden, name, address, phone, veteran_status):
        self.__iden = iden
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__veteran_status = veteran_status

    def print_patient(self):
        
        print("Name:",self.__name)
        print('Address:',self.__address)
        print('Phone:',self.__phone)
        print()
