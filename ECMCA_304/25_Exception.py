try:
    # code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # code that will be executed if the exception was raised
    print("Cannot divide by zero")
except Exception as e:
    # code that will be executed if any other exception was raised
    print("An error occurred:", e)
else:
    # code that will be executed if no exception was raised
    print("Result:", result)
finally:
    # code that will be executed no matter what
    print("Exiting try-except block")
