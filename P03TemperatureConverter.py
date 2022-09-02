"""
CSM 2170: P03TemperatureConverter

Complete this program to ask the user for the temperature in Celsius and convert it to Fahrenheit. The calculation
should be done as a float but when printing only display 2 digits after the decimal point. See Chapter 2 Programming
Exercise 9.
     9
F = --- C + 32
     5

Author(s): (Krishna Raju)
"""


def celsius_to_fahrenheit(celsius):
    """celcius to fahrenheit"""
    return ((9 / 5 * celsius) + 32)


if __name__ == "__main__":

    # Get temperature from the user (remove the pass statement)
    celsius_input = float(input('Enter degrees in celsius '))

    # Compute value to fahrenheit
    conversion = (9 / 5) * celsius_input + 32

    # Display result with only 2 digits after the decimal point
    print('The result in Fahrenheit is', format(conversion, '.2f'))