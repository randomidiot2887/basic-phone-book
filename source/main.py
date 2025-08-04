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
"""

max_contact_num = 100 # Holds the max number of contacts that can be stored in the program
contact_details = [["" for _ in range(6)] for _ in range(100)] # Array that stores the contact details of stored contacts
                    # For example, for one person, it could be [....['Aik', 'gn.fuvammulah@gmail.com', '+960 4084082', 'Donald Street', 'Gn.AEC', 'Alive']...]

def validate_details(email, phoneno, name):
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
    
    #Check if all the charectors in the phone number can be converted to numbers (except the first one)
    for num in phoneno:
        if (num != '+') and (num != ' '): # As there should be atleast 1 plus and 1 space in the format
            try:
                int(num) # Attempts to convert the charector to a integer
            except ValueError: # Wil only occur if the digit is not a number (Not numerical)
                valid_PhoneNo[3] = False # Sets the flag to false

def get_details():
    print('Input the following details about contact')
    contact_name = input('Contact Name\n(in format "FirstName, LastName"): - ')
    contact_email = input('Contact Email: - ')
    contact_phoneno = input('Contact Phone Number\n(in format "+CountryCode PhoneNumber"): - ')
    contact_address = input('Address of contact: - ')
    contact_work = input('Place they work at: - ')
    contact_status = input('Current status as of creation: - ')

