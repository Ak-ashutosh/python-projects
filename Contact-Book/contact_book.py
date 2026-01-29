# Contact Book

class contact:

    def __init__(self):
        self.contacts = {}
        self.home()

    def home(self):
        print("""
              ***************************Welcome TO PhoneBook***************************
              1. Add Contact
              2. Search Contact
              3. Update Contact
              4. Delete Contact
              5. Exit
              """)
        option = input('Select Choice : ')

        if option == '1':
            self.add_contact()

        elif option == '2':
            self.search_contact()

        elif option == '3':
            self.update_contact()

        elif option == '4':
            self.delete_contact()

        elif option == '5':
            print('Thanks for using PhoneBook')
            exit()
        else:
            print('Invalid Input')

    def add_contact(self):
        print('***************************Welcome TO PhoneBook***************************\n'
              ' ADD CONTACT DETAILS')
        user_firstname = input('Enter Firstname : ')
        user_lastname = input('Enter Lastname : ')
        userFullname = f'{user_firstname} {user_lastname}'

        user_phoneNumber = int(input('Enter Contact Number : '))
        user_address = input('Enter Address : ')

        self.contacts[userFullname] = {
            "FirstName": user_firstname,
            "LastName": user_lastname,
            "PhoneNumber": user_phoneNumber,
            "Address": user_address
        }
        print('Contact Saved Successfully!')
        self.home()

    def search_contact(self):
        print('***************************Welcome TO PhoneBook*************************** \n'
              ' SEARCH CONTACT DETAILS')
        user_firstname = input('Enter Firstname : ')
        user_lastname = input('Enter Lastname : ')
        print('-'*30)
        print('CONTACT DETAILS')
        userFullname = f'{user_firstname} {user_lastname}'

        user_key = self.contacts.get(userFullname)
        for key, value in user_key.items():
            print(f'{key:<15} : {value}')

        self.home()

    def update_contact(self):
        print('***************************Welcome TO PhoneBook*************************** \n'
              'UPDATE CONTACT DETAILS ')
        user_firstname = input('Enter Firstname : ')
        user_lastname = input('Enter Lastname : ')
        print('-'*30)
        userFullname = f'{user_firstname} {user_lastname}'

        user_key = self.contacts.get(userFullname)
        for key, value in user_key.items():
            print(f'{key:<15} : {value}')
        print('-'*30)
        new_fName = input('Enter New FirstName : ')
        new_lName = input('Enter New LastName : ')
        print('-'*30)
        new_FullName = f'{new_fName} {new_lName}'

        new_PhoneNumber = int(input('Enter New Phone Number : '))
        new_Address = input('Enter New Address : ')

        self.contacts[new_FullName] = {
            "FirstName": new_fName,
            "LastName": new_lName,
            "PhoneNumber": new_PhoneNumber,
            "Address": new_Address
        }

        print('Contact Details Updated Successfully!')
        self.home()

    def delete_contact(self):
        print('***************************Welcome TO PhoneBook*************************** \n'
              'DELETE CONTACT DETAILS ')
        user_firstname = input('Enter Firstname : ')
        user_lastname = input('Enter Lastname : ')
        userFullname = f'{user_firstname} {user_lastname}'

        del self.contacts[userFullname]
        print(f'{userFullname} Deleted Successfully')
        self.home()


contact()
