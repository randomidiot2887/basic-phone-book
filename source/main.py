"""
This is gonna be a basic python based phonebook program.
All data will be stored in primary memory with none stored in secondry memory
Its supposed to be basic, its goal is to improve my skills

Here are the features ill plan to add.
-------------------------------------
- Name of person
- Email of person
- Phone Number of person
    - In format "+AAA IEEEEEE"
- Address of person
- Work
- Status

These should be added.. per contact.
It should be able to handle up to 8000 contacts



First, we get contact info inputted from user   DONE
Then we validate it to make sure the enterd info is valid DONE
If so, then we store them in an array

We alow users to edit contacts and also update the status of the contacts
COntacts can also be deleted
They can also be searched with appropriate search termenology
and the program can be exit at some point
"""

max_contact_num = 100 # Holds the max number of contacts that can be stored in the program
contact_details = [["" for _ in range(6)] for _ in range(100)] # Array that stores the contact details of stored contacts
                    # For example, for one person, it could be [....['Aik', 'gn.fuvammulah@gmail.com', '+960 4084082', 'Donald Street', 'Gn.AEC', 'Alive']...]


def validate_details(email:str, phoneno:str):
    valid_Email = [False, False]
    valid_PhoneNo = [False, False, False, True]
    # Validate E-Mail
    for char in email:
        if char == '@':
            valid_Email[0] = True
        if (char == '.') and (valid_Email[0] == True): # If there is a fullstop after @ has been detected (like, in .com)
            valid_Email[1] = True
    # Validate PhoneNumber
    if phoneno[0] == '+': # Checks for + at posotion 0
        valid_PhoneNo[0] = True
    if phoneno[4] == ' ': # Checks for a ' ' at position 4
        valid_PhoneNo[1] = True
    if len(phoneno) == 12:  # If the length is exactly 12 digits
        valid_PhoneNo[2] = True
    
    # Check if all the charectors in the phone number can be converted to numbers (except the first one)
    for num in phoneno:
        if (num != '+') and (num != ' '): # As there should be atleast 1 plus and 1 space in the format
            try:
                int(num) # Attempts to convert the charector to a integer
            except ValueError: # Wil only occur if the digit is not a number (Not numerical)
                valid_PhoneNo[3] = False # Sets the flag to false
    # Return the correct boolean value depending on validity of data enterd
    if (valid_Email == [True, True]) and (valid_PhoneNo == [True, True, True, True]):
        return True
    else:
        return False

def get_details():
    while True: # Repeats until its broken out of
        print('Input the following details about contact') # Prompts user to input details
        contact_name = input('Contact Name\n(in format "FirstName, LastName"): - ') # Get the name of the contact
        contact_email = input('Contact Email: - ') # Get contacts email
        contact_phoneno = input('Contact Phone Number\n(in format "+CountryCode PhoneNumber"): - ') # Gets the contacts phone number
        contact_address = input('Address of contact: - ') # Gets the contacts address
        contact_work = input('Place they work at: - ') # Gets the name of the workplace they work at
        contact_status = input('Current status as of creation: - ') # Get the initial status of the contact
        if validate_details(contact_email, contact_phoneno): # Checks if the email and phone number are in a valid format
            break # if so, exits the while loop
        else:
            print("Invalid data was enterd. Please re-enter") # If not, prompts the user to re-enter
    return [contact_name, contact_email, contact_phoneno, contact_address, contact_work, contact_status] # Returns the data in the approved format

def store_details(details):                                     # Stores details of new_contact in the array contact_details
    if len(details) != 6:                                       # makes sure the passed on list details[] is only 6 elements long
        raise TypeError                                         # if not, raise TypeError (for debugging)
    for element in range(len(contact_details)):                 # For each element in the range of the total values of contact_details[]
        if contact_details[element] == ["" for _ in range(6)]:  # if that element of the array is empty                      
            for data in range(6):                               # If its empty, loop for ever data to be stored
                contact_details[element][data] = details[data]  # Store them one by one into the array
            return element                                      # Exits function on succesful entry, returning index of the newly added contact

# print(store_details(get_details())) Code used for testing the first 3 functions, works fine.

def display_contact_details(contact_index:int):                          # Displays details of one contact
    if (contact_index >= len(contact_details)) or (contact_index < 0):   # if the index value is not withn the length of the array
        raise IndexError                                                 # Then raise IndexError
    # Prints all the details of the contact in the terminal and exits
    print(f"Contact Index: - {contact_index}")
    print(f"Contact Name: - {contact_details[contact_index][0]}")
    print(f"Contact E-Mail: - {contact_details[contact_index][1]}")
    print(f"Contact Phone-No: - {contact_details[contact_index][2]}")
    print(f"Contact Address: - {contact_details[contact_index][3]}")
    print(f"Contact Work: - {contact_details[contact_index][4]}")
    print(f"Contact Status: - {contact_details[contact_index][5]}")
    # End of procedure

def replace_details(details:list, contact_index:int):               # Replaces details of existing_contact in the array contact_details
    if len(details) != 6:                                           # makes sure the passed on list details[] is only 6 elements long
        raise TypeError                                             # if not, raise TypeError (for debugging)
    if contact_details[contact_index] != ["" for _ in range(6)]:    # if that element of the array is not empty                      
        for data in range(6):                                       # If its not empty, loop for every data to be stored
            contact_details[contact_index][data] = details[data]    # Store them one by one into the array
        return contact_index                                        # Exits function on succesful entry returning element of existing edited contact
    else:                                                           # if the index is of an empty position (invalid)
        raise IndexError                                            # Raises IndexError

def del_contact(contact_index:int):                                 # Deletes the contact and their info in the index provided
    if (contact_index < 0) and (contact_index >= max_contact_num):  # If the index is out of range
        raise IndexError                                            # Raises IndexError
    else:                                                           # If index is in range
        contact_details[contact_index] = ["" for _ in range(6)]     # Nulls out the info stored at index

def change_status(contact_index:int):
    if (contact_index < 0) and (contact_index >= max_contact_num):  # If the index is out of range
        raise IndexError                                            # Raises IndexError
    
    print(f"Contact Name is '{contact_details[contact_index][0]}'") # Prints the name of the contact
    print(f"Contacts former status is '{contact_details[contact_index][5]}'")           # Prints the former status of the contact
    new_status = input(f"Input the new status for contact no {contact_index}\n: - ")    # Gets the new status from user input
    contact_details[contact_index][5] = new_status                  # Stores the new status in the array

def search_contacts(promt:str, no_results:int):
    # i hate myself, I hate myself, I Hate Myself, I HATE MYSELF'
    
