from operator import truediv
import Exercise as ex

def main():
    person = ex.Person('John Smith','123 Street','123-456-7890')
    customer = ex.Customer('Regular Guy', '456 Road','098-765-4321',1,True)
   
    person.print_person()
    customer.print_person()

main()
