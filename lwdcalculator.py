class Calculator:
    user_response : str
    result : str

    def get_input(self):
      ''' get input '''
      self.user_response = input("Please enter two numbers : ")
    
      values = self.user_response
      while isinstance(values, str):
          try:
            values = [int(i) for i in self.user_response.split()]
          except ValueError:
            self.user_response = input("Input should contain numbers only, please try again : ")                   
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
