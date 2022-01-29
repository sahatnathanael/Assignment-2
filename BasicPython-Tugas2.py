import os
contactList = []
numList = []
def showContacts() :
    if(len(contactList)) == 0 :
        print("Kontak kosong")
    else : 
        os.system("clear")
        print("Contact List")
        for i in range (0, len(contactList)) :
            print("Nama\t\t\t : ", contactList[i])
            print("Phone Number\t\t : ", numList[i])
        os.system("pause")
        menu()

def addContacts () :
    os.system("cls")
    contact = input("Name: ")
    numContact = input("Phone Number: ")
    contactList.append(contact)
    numList.append(numContact)
    print("Successfully added new contact")
    os.system("pause")
    menu()

def menu() : 
    os.system("cls")
    print("Welcome to Contacts!")
    print("---Menu---")
    print("1. Contact List")
    print("2. Add New Contacts")
    print("3. Close")
    x = int(input("Choose menu: "))
    if x == 1 : showContacts()
    elif x == 2 :  addContacts()
    elif x == 3 : print("End of program, goodbye!")
    else : print("Menu is unavailable")
menu()