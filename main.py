# To Do:
# - Probably try without using eval()

while True:
    expression = input("Please enter an expression : ")
    sanitized =  "".join([x for x in expression if x in "123456789-./*() "])
    if sanitized == expression:
        print (eval(expression))
        break
    else:
        print ("Please enter a valid expression.")
