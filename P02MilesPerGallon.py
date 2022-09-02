"""
CSM 2170: P02MilesPerGallon

A vehicle's miles-per-gallon (MPG) can be calculated with the following formula:
         Miles driven
MPG = -------------------
      Gallons of gas used

Complete this program to ask the user for the number of miles driven and the gallons of gas used. It should calculate
the  vehicle's MPG and display the result. Fractional values should be truncated. If the MPG is 42.2 then just return
and display 42. See Chapter 2 Programming Exercise 7.

Author(s): (Krishna Raju)
"""


def mpg(miles, gallons):
    """miles per gallon"""
    return miles // gallons


if __name__ == "__main__":
    # Remove the pass statement. It is a placeholder for your code. A pass statement is a nop
    # ("no op" short for no operation) that does nothing.

    # Get data from the user.
    miles_driven = input('Enter the number of miles driven ')

    # Convert to an int
    miles_driven = int(miles_driven)

    # Get data from the user
    gallons_used = input('Enter the number of gallons used ')

    # Convert to an int
    gallons_used = int(gallons_used)

    # Display result
    print(' Your current mpg is', mpg(miles_driven, gallons_used))