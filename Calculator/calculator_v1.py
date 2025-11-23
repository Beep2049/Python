class Calculator:
    def __init__(self):
        #On/Off Variable
        calc_on = True    
        while calc_on:

            # Inputs:
            self.num1 = float(input("Enter the first number: "))
            self.operation = input("Enter the operation: ").strip()
            self.num2 = float(input("Enter the second number: "))

            #Operations:
            #Add
            self.addition = self.num1 + self.num2

            #Subtract
            self.subtract = self.num1 - self.num2

            #Multiply
            self.multiply = self.num1  * self.num2

            #Divide
            self.divide = self.num1  / self.num2
            if self.num2 == 0:
                print("Cannot divide by zero") 

            #Exponent
            self.exponent = self.num1 ** self.num2
            if self.num2 == 0:
                self.exponent = 1



            #Output:    
            if self.operation == "+":
                print(f'The answer to {self.num1} plus {self.num2} is {self.addition}') 
            elif self.operation == "-":
                print(f'The answer to {self.num1} minus {self.num2} is {self.subtract}') 
            elif self.operation == "*":
                print(f'The answer to {self.num1} multiplied {self.num2} is {self.multiply}') 
            elif self.operation == "/":
                print(f'The answer to {self.num1} divide {self.num2} is {self.divide}')
            elif self.operation == "**":
                print(f"{self.num1} to the power of {self.num2} equal {self.exponent}") 
            else:
                print("Invalid operation")
                self.operation = input("Enter the operation: ").strip()



            #New Operation:
            keep_going = input("Another operation?: ").lower().strip()
            if keep_going == 'no':
                calc_on = False
                break
            elif keep_going == 'yes':
                print()
            else:
                print("Please enter yes or no")

# Start   
Calculator()
        
        