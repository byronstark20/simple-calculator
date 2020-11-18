class Calculator:
    user_response : str
    result : str

    def get_input(self):
      ''' get input '''
      values = input("Please enter two numbers : ")

      while isinstance(values, str):
          try:
            values = [int(i) for i in values.split()]
          except ValueError:
            values = input("Input should contain numbers only, please try again : ")                    
      self.user_response = values
      return values

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