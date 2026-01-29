# Student Management System

class student:

    def __init__(self):
        self.stud_dict = {}
        self.std_marks = []
        self.home()

    def home(self):
        print("""
              *****************************Welcome to Student Management System*****************************
              1. Add Students
              2. View Students
              3. Calculate Average & Grade
              4. Exit
              """)
        choice = input('Enter Your option : ')

        if choice == '1':
            self.add_std()

        elif choice == '2':
            self.view_std()

        elif choice == '3':
            self.cal_avg_grade()

        elif choice == '4':
            print('Thanks for using')
            exit()
        else:
            print('Invalid Input')

    def add_std(self):
        user_firstName = input('Enter FirstName : ')
        user_lastName = input('Enter lastName : ')
        user_high_qual = input('Enter Highest Qualification : ')
        user_field = input('Enter Field : ')

        user_subMark01 = int(input('Enter Marks Sub 01 : '))
        user_subMark02 = int(input('Enter Marks Sub 02 : '))
        user_subMark03 = int(input('Enter Marks Sub 03 : '))
        user_subMark04 = int(input('Enter Marks Sub 04 : '))

        self.std_marks = [user_subMark01, user_subMark02,
                          user_subMark03, user_subMark04]

        userName = f'{user_firstName} {user_lastName}'
        # self.stud_dict[userName] = {user_firstName,
        #                           user_lastName, user_high_qual, user_field, self.std_marks}
        self.stud_dict[userName] = {
            "first_name": user_firstName,
            "last_name": user_lastName,
            "qualification": user_high_qual,
            "field": user_field,
            "marks": self.std_marks,
        }

        print('Student Data Added Successfully!')
        self.home()

    def view_std(self):
        user_firstName = input('Enter FirstName : ')
        user_lastName = input('Enter LastName : ')

        userName = f'{user_firstName} {user_lastName}'
        print(self.stud_dict[userName])
        self.home()

    def cal_avg_grade(self):
        user_firstName = input('Enter FirstName : ')
        user_lastName = input('Enter LastName : ')

        userName = f'{user_firstName} {user_lastName}'
        if userName in self.stud_dict:
            avgGrade = round(sum(self.std_marks) / len(self.std_marks), 2)

            print(f'Average Grade of {userName} is -> {avgGrade}')
        self.home()


student()
