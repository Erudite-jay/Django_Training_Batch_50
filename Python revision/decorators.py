#zero division error
def handle_zero_division(func):
    def wrapper(a,b):
        try:
            return func(a,b)
        except ZeroDivisionError:
           print("Cannot divide by zero")
    return wrapper
        
# extend funnctionality 
@handle_zero_division
def divide(a,b):
    return a/b

divide(10,0)