class Contact:
  '''
  A class concerning contact information\n
  Attributes:
  (str) first_name: The first name of the contact
  (str) last_name: The last name of the contact
  (str) phone: The phone number of the contact
  (str) address: The address of the contact
  (str) city: The city of the contact
  (int) zip: The zip code of the contact
  '''

  def __init__(self,fn,ln,ph,addr,city,zip):
    '''
    Constructs a contact\n
    Parameters:\n
    fn - First name of the contact\n
    ln - Last name of the contact\n
    ph - Phone number of the contact\n
    addr - Address of the contact\n
    city - City of the contact\n
    zip - zip code of the contact
    '''
    self.first_name = fn
    self.last_name = ln
    self.phone = ph
    self.address = addr
    self.city = city
    self.zip = int(zip)

  def __lt__(self, other):
    '''
    Compares two contacts by last names, then by first names if tied
    Returns true if the first contact comes before the other
    (Contact) Other - Contact to be compared
    '''
    # A string is greater if it comes later in ascii
    if(self.last_name < other.last_name):
      return True
    elif(self.last_name > other.last_name):
      return False
    else:
      #Last names are equal, this returns a bool
      return self.first_name < other.first_name

  def __str__(self):
    '''
    Returns a string representation of the contact
    '''
    display = self.first_name + " " + self.last_name + "\n" + self.phone + "\n"
    display += self.address + "\n" + self.city + " " + str(self.zip)
    return display

  #Called off a cast to type repr
  def __repr__(self):
    '''
    Returns a string formatted to be read off of a file
    '''
    temp = self.first_name + "," + self.last_name + "," + self.phone + ","
    temp += self.address + "," + self.city + "," + str(self.zip)
    return temp

    #temp = f"{self.first_name}, {self.last_name}, {self.phone}, "