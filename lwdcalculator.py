class Calculator:
    user_response : str
    result : str

    def get_input(self):
        ''' get input '''
        self.user_response = input("Please enter your calculation : ")

    def calculate_guy(self):
        '''process user_response'''
        pass

    def calculate_tuti(self):
        '''process user_response'''
        pass

    def calculate_bw(self):
        '''process user_response'''
        pass

    def get_result(self):
        '''output'''
        print(f"Result is {self.result}.")