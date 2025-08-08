def validate_details(email, phoneno):
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

print(validate_details("gn.fuvammulah@gmail.com", "+960 9584082"))