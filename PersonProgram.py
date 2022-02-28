import PersonClass as P

def main():

    Personinfo = P.Person("Blake Ehlinger",
             "102 Lane", "832-555-0219")
    Customerinfo = P.Customer("Blake Ehlinger",
             "102 Lane", "832-555-0219", 102, True)

             
    Personinfo.print_person()
    Customerinfo.print_person()
main()