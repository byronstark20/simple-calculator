from lwdcalculator import Calculator

if __name__ == "__main__":
    calc = Calculator()
    calc.get_input()    
    # choose a calculation method
    calc.calculate_default()
    calc.get_result()