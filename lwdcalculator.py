class Calculator:
    user_response : str
    result : str

    def get_input(self):
        ''' get input '''
        self.user_response = input("Please enter your calculation : ")

    def calculate_guy(self) -> float:
        '''process user_response string and returns calculated result'''
        pass

    def calculate_tuti(self) -> float:
        '''process user_response string and returns calculated result'''
        pass

    def calculate_bw(self) -> float:
        '''process user_response string and returns calculated result'''
        pass

    def get_result(self):
        '''output'''
        print(f"Result is {self.result}.")