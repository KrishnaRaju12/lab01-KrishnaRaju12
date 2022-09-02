"""
CSM 2170: P05CompoundInterest

You are to make a program to calculate compound interest. Your program must ask the user to input:

* The amount of the principle originally deposited as a non-negative float (e.g. 1013.56 for $1013.56 or whatever
  currency the account is in)
* The annual interest rate as a percentage (a float) (e.g. the user would type 3.15 for 3.15% which will need to be converted
  into the decimal .0315 for the calculation)
* The number of times per year the interest is compounded as a positive integer
* The number of years the account will earn interest as a positive integer

Then the program should calculate and display the amount of money that will be in the account after the specified
number of years. See Chapter 2 Programming Exercise 14 for more details and the formula for this type of compound
interest.

Author(s): (Krishna Raju)
"""


def future_value(principle, rate, times_compounded_per_year, years):
    return principle * (1 + (rate / 100) / times_compounded_per_year) ** (times_compounded_per_year * years)


if __name__ == "__main__":

    # Principle ammount

    principle_amount = float(input('Enter the amount of principle originally deposited '))
    # Interest rate
    interest_rate = float(input('Enter the annual rate '))

    interest_rate = (interest_rate) / 100

    # Number of years that the interest is compounded
    compound_rate = float(input('Enter the number of years the interest is compounded '))

    # Number of years the account will earn interest
    interest_years = float(input('Enter the number of years the account will earn interest '))

    print('The value of the account will be ', format(future_value(principle_amount, interest_rate, compound_rate, interest_years), '.2f'))