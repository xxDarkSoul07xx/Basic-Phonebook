phonebook = {}
contact_name = ""
edit = ''
choice = 0

print("Welcome to your phonebook!")
print("Press 1 to add a contact.")
print("Press 2 to delete a contact.")
print("Press 3 to edit a contact.")
print("Press 4 to view your phonebook.")
print("Press 5 to quit.")


while choice != 5:
    choice = int(input("Enter the number of the action you would like to do: "))
    if choice == 1:
        contact_name = input("What is the contact's name? ").lower()
        contact_age = input("What is the contact's age? ")
        contact_number = input("What is the contact's number?: ")
        phonebook[contact_name] = {
            "age:": contact_age,
            "number:": contact_number
        }
    elif choice == 2:
        contact_name = input("What is the name of the contact you would like to delete?: ").lower()
        if contact_name in phonebook:
            phonebook.pop(contact_name)
            print("Contact deleted")
        else:
            print("Contact name not found")
    elif choice == 3:
        new_name = ''
        new_number = ''
        new_age = 0
        contact_name = input("What is the name of the contact you would like to edit?: ").lower()
        if contact_name in phonebook:
            print(phonebook[contact_name])
            edit = input("What would you like to edit?: ").lower()
            if edit == "name":
                new_name = input("What is the new name?: ").lower()
                phonebook[new_name] = phonebook.pop(contact_name)
                print(f"Contact updated: {phonebook[new_name]}")
            elif edit == "number":
                new_number = input("What is the new number?: ")
                phonebook[contact_name]["number:"] = new_number
                print(f"Contact updated: {phonebook[contact_name]}")
            elif edit == "age":
                new_age = input("What is the new age (enter an integer)?: ")
                phonebook[contact_name]["age:"] = new_age
                print(f"Contact updated: {phonebook[contact_name]}")
            else:
                print("I do not understand.")
        else:
            print("Contact name not found.")
    elif choice == 4:
        print(phonebook)
    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("I do not understand.")
