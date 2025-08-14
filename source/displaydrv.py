"""
This script should help in managing the hud features of it (like the display function) without breaking the main program
Should helpt with modularity, and will incease complexity
Its a module that should be imported to main file when running,
if not, itll not work.
"""

def contacts_book():
    """
    This should display the contacts details in the following format, in a page by page basis
    ----------------------------------------------------------------------------------------
    [Contact no 69]
    Name:       John Doe
    E-Mail:     test@example.com
    PhoneNo:    +960 9122418
    Address:    Pivet Drive
    Work:       Garbage collector
    Status:     Arested in deathrow for 10 years as he was a sex offender
    ['a': Prev-Page, 's': Next-Page, 'e': Edit details, 'd':Delete, 'q': Change status, 'w':Go to contactID]

    Input option: - a
    ... clears screen and shows details of contact#68, in same style
    ... that is if contact 68 exists. if not, itll show the most nearest number below 69 that exists.
    !!! if none, itll show that its not avalable. if no contact there, msg will apper
    ----------------------------------------------------------------------------------------
    Now to implement this, ill have to use input() as thats whats withn my skill... so itll not be as good....
    it should still work
    """



def display_contacts(contact_no):   # Responsible for displaying the contacts in that format stated in docstring from LN 7-> 26
    print(f"[Contact no {contact_no}]"
            f"Name:     {contact_details[contact_no][0]}\n"
            f"E-Mail:   {contact_details[contact_no][1]}\n"
            f"PhoneNo:  {contact_details[contact_no][2]}\n"
            f"Address:  {contact_details[contact_no][3]}\n"
            f"Work:     {contact_details[contact_no][4]}\n"
            f"Status:   {contact_details[contact_no][5]}\n"
            f"['a': Prev-Page, 's': Next-Page, 'e': Edit-details, 'd': Delete, 'q': Change-status, 'w': Go to contactID]"
        )

def get_input_next_option():
    """
    Gets user unput and makes sure its valid, below array valid_choice() has valid options user can choose
    """
    valid_choice = [
        'a', # Prev-Page
        's', # Next-Page
        'e', # Edit Details
        'd', # Delete
        'q', # Change-Status
        'w'  # Go to contactID
         ]
    option = input("Option: - ").lower()
    if (len(option) == 1) and (option in valid_choice):
        return option
    else:
        raise ValueError(f"{option} is not a valid option in this function")






if __name__ == "__main__":   # If the user tries to run this manually
    print("This is supposed to be imported into the main loop where the main code will handle it. Dont run it seperately")
else: # If its runing from an imported program
    print("display driver loaded succesfully, execution can contnue, no issues")
