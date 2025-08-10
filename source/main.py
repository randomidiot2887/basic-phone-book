"""
This is gonna be a basic python based phonebook program
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
If so, then we store them in an array DONE

We alow users to edit contacts and also update the status of the contacts DONE
COntacts can also be deleted DONE
They can also be searched with appropriate search termenology DONE
We also have a book like scrolling system for the contacts TODO
and the program can be exit at some point
"""

"""
Libraries imported
------------------
1: - os
    handles commands related to the OS.
    os.system() is used alot in this code, thus this is neccecery for execution
2: - platform
    platform.system() is used to determine what OS the script is running on
    This is needed as some console commands are used for stuff like...
    ... clearing the screen
"""
import os
import platform



max_contact_num = 100 # Holds the max number of contacts that can be stored in the program
contact_details = [["" for _ in range(6)] for _ in range(max_contact_num)] # Array that stores the contact details of stored contacts
                    # For example, for one person, it could be [....['Aik', 'gn.fuvammulah@gmail.com', '+960 4084082', 'Donald Street', 'Gn.AEC', 'Alive']...]

# Stuff needed to make this program, OS Independent
# -------------------------------------------------
os_name = platform.system()     # gets the name of the OS using platform.system()

# Cleares the screen
def cls():                          # A procedure that handles clearing the screen while being platform independent
    if os_name == 'Windows':        # if the OS is Windows
        os.system('cls')            # Use the command 'cls'
    elif os_name == "Linux":        # if the os is Linux
        os.system('clear')          # use the command 'clear'
    elif os_name == 'Darwin':       # if the OS is Darwin (macOS)
        os.system('clear')          # use the command 'clear'
    else:                           # If the OS is unditermined...
        raise OSError               # Raise the error OSError (This hasnt been made for your OS)


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

def search_contacts(prompt:str, no_results:int):               # Function to search thru contacts array for key words and return a certain amount of results
    # i hate myself, I hate myself, I Hate Myself, I HATE MYSELF'
    """
    DEV EXPLANATION
    -----------------
    This algorithm will first select the first letter of the promt enterd by the user
    Then it iterates thru every single element in contact_details[]... 
    ...and compares every single letter of every field to the first letter of prompt
    if the letters match, the contacts index (row) is appended to results[] with a score, of 1
    then it iterates theu the rest of the array letter by letter
    if a element of a contact has more matching letters to the prompt, itll get a higher score...
    ... by searching thru the results to see if they already exist
    if they do, their score is incremented by 1 for every letter matched
    once results[] has been found...
    a bubble sort is performed to arrange contact IDs in decending order of their scores
    Then, itll get the results and try to identify the results with the highest scores and appends the ids...
    ... of the highest scoring contacts to final_results[].
    Itll ONLY find the highest scoring contacts and will try to return only the number of results requested.
    If the resquested number of results is not found, it sets max_results_found to false and returns it along with the requested contacts,
    If the requested number of results is found, it sets max_results_found to true and returns it along with the required contacts
    ------------------
    ISSUES
    ------
    This is a very inefficient algorithm. ill have to improve it once i learn more
    Bubble sort squares time for every contact added. This can add up to alot
    and the searching method i used is also very rudementry and unnececerily complex
    To Sum Up: - This can be improved alot.
    """
    results = []                                               # declares array results[]
    for char_prompt in prompt:                                 # Compares every single charector in prompt
        for row in range(max_contact_num):                     # Iterates thru every row in the array
            for column in range(6):                            # iterates theu every column in array
                for char_list in contact_details[row][column]: # Comares every single charector in the element in list
                    if char_list == char_prompt:               # if the charector matches
                        found = False                          # initialises found as False
                        if len(results) != 0:                  # If results is not empty
                            for element in range(len(results)):# Iterates thru results
                                if results[element][0] == row: # if the results contains the row already
                                    results[element][1] += 1   # Add 1 to its credibility score
                                    found = True               # sets found to true
                                    break                      # breaks out of the linier search
                            if not found:                      # if not found
                                results.append([row, 1])       # Appends a new entry to results
                        else:                                  # if results is empty
                            results.append([row, 1])           # Appends a new entery to results
    if len(results) > 0:
        while True:                                            # Repeats until loop
            swap = False                                       # Sets the SWAP flag to false
            for element in range(len(results) - 1):            # Repeats for every element except the last one
                if results[element][1] < results[element+1][1]:    # If the former element is smaller then the next element
                    results[element+1], results[element] = results[element], results[element+1] # Swaps elements values
                    swap = True                                # Sets swap to True
            if not swap: break                                 # If no swap has occured, exit the loop, as data has been sorted
    final_results = []                                         # Declares list final_results
    max_results_found = True                                   # Sets the flag max_results_found to True
    counter = 0                                                # Initialises counter variable to 0
    for result in results:                                  # Iterates thru every result found from 0
        counter += 1                                           # Incrememnts the counter by 1
        final_results.append(result[0])                           # Appends one result to final_results[]
        if counter == no_results: break                       # If the number of max results to return has been reached, exit loop
    if counter != no-results:                                 # If the maximum amount of results hasnt been found (like, less then max results)
        max_results_found = False                              # Sets the max_results_found flag to False
    return [final_results, max_results_found]                  # Returns data in format [{Results found in a list, like 0, 1, 2, 3}, {the boolean value in max_results_found}]


