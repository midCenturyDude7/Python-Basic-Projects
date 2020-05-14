"""
File: temp_converter.py
This program asks the user to choose whether to convert a temperature in Fahrenheit or Celsius and
then calculates the requested conversion and prints it to the console.
"""


def main():

    # Local variables to set constraints for user input to 'F' and 'C'
    fahrenheit_temp = "F"
    celsius_temp = "C"

    # Program will reload after each pass through, until user manually exits
    while True:
        # Asks user to choose which temperature to convert to
        user_input_temp = input("Choose which temp to convert to. Enter an 'F' for Fahrenheit or a 'C' for Celsius: ")
        # Conditional that checks and validates if the user chose "F'
        if user_input_temp == fahrenheit_temp:
            # Asks the user to enter the temperature
            user_input_num = int(input("Okay! Enter the temperature you'd like to convert to Celsius: "))
            # Calls the fahrenheit_to_celsius() function and passes the user input as an argument via the
            # user_input_num parameter
            fahrenheit_conversion = fahrenheit_to_celsius(user_input_num)
            # Prints result to screen
            print("You entered " + str(user_input_num) + " degrees Fahrenheit. It converts to...")
            print("")
            print(str(fahrenheit_conversion) + " degrees Celsius.")
            print("")
        # Conditional that checks and validates if the user chose "C'
        elif user_input_temp == celsius_temp:
            # Asks the user to enter the temperature
            user_input_num = int(input("Okay! Enter the temperature you'd like to convert to Fahrenheit: "))
            # Calls the celsius_to_fahrenheit() function and passes the user input as an argument via the
            # user_input_num parameter
            celsius_conversion = celsius_to_fahrenheit(user_input_num)
            # Prints the result to the screen
            print("You entered " + str(user_input_num) + " degrees Celsius. It converts to...")
            print("")
            print(str(celsius_conversion) + " degrees Fahrenheit.")
            print("")
        # Conditional that handles invalid user input that isn't either an 'F' or a 'C'
        else:
            print("INVALID OPTION! Try again, please.")


# Calculates Fahrenheit to Celsius based on conversion equation
# and returns the variable, fahrenheit_conversion to the main() function
# to be processed as part of the user input/function call/print to console
def fahrenheit_to_celsius(user_input_num):
    fahrenheit_conversion = int((user_input_num - 32) * 5 / 9)
    return fahrenheit_conversion


# Calculates Celsius to Fahrenheit based on conversion equation
# and returns the variable, celsius_conversion to the main() function
# to be processed as part of the user input/function call/print to console
def celsius_to_fahrenheit(user_input_num):
    celsius_conversion = int((user_input_num * 1.8) + 32)
    return celsius_conversion


if __name__ == '__main__':
    main()
