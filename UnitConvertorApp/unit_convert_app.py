
# UNIT Convertor APP

class unit:
    def __init__(self):
        self.home()

    def home(self):
        print("""
              *******************************Welcome To Unit Convertor *******************************
              1 km ↔ miles
              2 °C ↔ °F
              3 kg ↔ pounds
              """)
        choice = input('Enter Choice: ')

        if choice == '1':
            self.km_to_mil()
        elif choice == '2':
            self.degree_to_fereih
        elif choice == '3':
            self.kg_to_pounds
        else:
            print('Thank You For Using Our Convertor')

    def km_to_mil(self):
        user_value = int(input('Enter in Km : '))
        print(f'{user_value}km is = ', user_value*0.621371, 'miles')
        print('Thank You For Using Our Convertor')

    def degree_to_fereih(self):
        user_value = int(input('Enter in degree : '))
        print(f'{user_value}°C is = ', user_value*32, '°F')
        print('Thank You For Using Our Convertor')

    def kg_to_pounds(self):
        user_value = int(input('Enter in kgs : '))
        print(f'{user_value}kgs is = ', user_value*2.20462, 'pounds')
        print('Thank You For Using Our Convertor')


a = unit()
