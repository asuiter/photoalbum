


class userinput():

    user_input = 0
    user_input_answer = None
    yes = 'y'
    no = 'n'

    viewcount = 0

    #Get user input for Album ID and make sure it is valid
    @classmethod
    def get_user_input(cls):
        while True:
            cls.user_input = input('Enter AlbumId Number 1-100:')
            
            try:
                user_input_value = int(cls.user_input)
            except:
                print('This is not a valid number, Please enter a number 1-100')
                continue
            if user_input_value < 1:
                print('Please enter a number 1-100')
                continue
            if user_input_value > 100:
                print('Please enter a number 1-100')
                continue
            return cls.user_input
            break

    @classmethod
    def get_user_input_answer(cls):
    
        while True:    
            cls.user_input_answer = input('Would you like to view another album? Y/N:')
            user_input_response = str(cls.user_input_answer).lower()
            if user_input_response == cls.yes:
                cls.viewcount = cls.yes
                return cls.viewcount
            elif user_input_response == cls.no:
                cls.viewcount = cls.no
                print('Goodbye')
                return cls.viewcount
            else:
                print('Please enter Y/N')
                continue
            break
        



       

