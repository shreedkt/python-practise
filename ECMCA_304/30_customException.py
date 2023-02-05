class CustomException(Exception):
    pass

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        raise CustomException("Cannot divide by zero")
    return result

try:
    divide(10, 0)
except CustomException as e:
    print(e)
