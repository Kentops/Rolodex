'''
Digital Rolodex
2/21/2024
An online rolodex capable of sotring and creating contacts.
'''
import contact
import check_input


#Don't forget to close files
def read_file(filename):
  '''Reads the file and returns a list of contacts'''

  contacts = []
  with open(filename) as file:
    for line in file:
      temp = line.strip('\n')  #line is read-only
      i = temp.split(",")
      new_contact = contact.Contact(i[0], i[1], i[2], i[3], i[4], i[5])
      contacts.append(new_contact)
    file.close()
  contacts.sort()
  return contacts


def write_file(contacts):
  '''Writes each contact to the file'''

  with open("addresses.txt", 'w') as file:
    for person in contacts:
      file.write(repr(person) + '\n')
    file.close()


def get_menu_choice():
  '''Displays the menu choice to the user and returns the user's choice'''

  print("\nRolodex Menu:")
  print("1. Display Contacts")
  print("2. Add contact")
  print("3. Search contact")
  print("4. Modify contact")
  print("5. Save and quit\n")
  choice = check_input.get_int_range("", 1, 5)
  return choice


def modify_contact(con):
  '''Modifies the contact the user wants to modify'''

  modifying = True
  while modifying:
    print("Modify Menu:")
    print("1.First Name")
    print("2.Last Name")
    print("3.Phone")
    print("4.Address")
    print("5.City")
    print("6.Zip")
    print("7.Save")
    choice = check_input.get_positive_int("Enter your choice: ")
    if choice == 1:
      con.first_name = input("Enter first name: ")
    elif choice == 2:
      con.last_name = input("Enter last name: ")
    elif choice == 3:
      con.phone = input("Enter phone #: ")
    elif choice == 4:
      con.address = input("Enter address: ")
    elif choice == 5:
      con.city = input("Enter city: ")
    elif choice == 6:
      con.zip = input("Enter zip: ")
    elif choice == 7:
      modifying = False
      return

    else:
      print("Invalid input - should be an integer.")
      
    print()


def main():
  contacts = read_file("addresses.txt")

  browsing = True
  while browsing:
    choice = get_menu_choice()
    if choice == 1:
      print(f"Number of contacts: {len(contacts)}")
      for index in range(len(contacts)):
        print(f"{index + 1}. {contacts[index]} \n")

    elif choice == 2:
      print("Enter new contact:")
      first_name = input("First Name: ")
      last_name = input("Last Name: ")
      phone = input("Phone #: ")
      address = input("Address: ")
      city = input("City: ")
      zip = check_input.get_positive_int("Zip: ")
      new_contact = contact.Contact(first_name, last_name, phone, address, city, zip)
      contacts.append(new_contact)
      contacts.sort()

    elif choice == 3:
      search_type = check_input.get_int_range(
          "Search:\n1.Search by last name\n2.Search by zip\n", 1, 2)
      if search_type == 1:
        last_name = input("Enter last name: ")
        found = False
        for con in contacts:
          if con.last_name == last_name:
            print()
            print(con)
            found = True
        if not found:
          print("No contact found")
      else:
        zip = check_input.get_positive_int("Enter zip:")
        found = False
        for con in contacts:
          if con.zip == zip:
            print()
            print(con)
            found = True
        if not found:
          print("No contact found")

    elif choice == 4:
      first_name = input("Enter first name: ")
      last_name = input("Enter Last name:")
      found = False
      for con in contacts:
        if con.first_name == first_name and con.last_name == last_name:
          print("\n" + str(con) + "\n")
          modify_contact(con)
          contacts.sort()
          found = True
          break
      if not found:
        print("Contact not found.")
        
    else:
      #Choice = 5
      browsing = False
      print("Saving File...")
      write_file(contacts)
      print("Ending Program")


main()
