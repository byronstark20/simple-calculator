class Calculator:
    user_response : str
    result : float

    def __init__(self):
        self.result = 0

    def get_input(self):
      ''' get input and stores in user_response '''
      self.user_response = input("Please enter two numbers : ")

    def calculate_default(self) -> float:
        '''legacy code'''
        values = self.user_response
        while isinstance(values, str):
            try:
                values = [int(i) for i in values.split()]
            except ValueError:
                values = input("Input should contain numbers only, please try again : ") 

        print("""
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        """)

        operation = input("Please choose an operation : ")

        while isinstance(operation, str):
            try:
                operation = int(operation)
            except ValueError:
                operation = input("Input should contain numbers only, please try again : ")

        # can be simplified with dictionary
        if operation == 1:
            result = values[0] + values[1]
            print(result)
        else:
            print("No valid operation chosen.")

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