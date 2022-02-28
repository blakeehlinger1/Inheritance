

class Person:

    def __init__(self, name, address, phone):
        self.__name_ = name
        self.__address_ = address
        self.__phone_ = phone
    def print_person(self):
        print(self.__name_, self.__address_, self.__phone_)

class Customer(Person):
    def __init__(self, name, address, phone, custnum,mail):
        Person.__init__(self, name, address, phone)

        self.__custnum =custnum
        self.__mail = mail
    def print_person(self):
        Person.print_person(self)

        print(self.__custnum,self.__mail)

    
    