class Procedure:

    def __init__(self, name, date, practitioner,charges,iden ):
        self.__name = name
        self.__date = date
        self.__practitioner  = practitioner 
        self.__charges = charges
        self.__iden = iden
    
    def print_procedure(self):
        print()
        print('Procedure:',self.__name)
        print('Date:',self.__date)
        print('Practitioner:',self.__practitioner)
        print('Charge:', '$',self.__charges)
        print()
        

    