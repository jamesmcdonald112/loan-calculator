import math
import argparse

# Argument parser
parser = argparse.ArgumentParser(description="This program prints information regarding loan "
                                             "payments, principal amount, and loan lengths based "
                                             "on information provided by the user.")

# Add optional arguments
parser.add_argument("--principal", type=float, help="Principal loan amount")
parser.add_argument("--periods", type=int, help="Total number of payments in months")
parser.add_argument("--payment", type=float, help="Monthly payment amount")
parser.add_argument("--interest", type=float, required=True, help="Annual interest rate as a "
                                                                  "floating point number without the % sign")

# Parse the arguments
args = parser.parse_args()


def calculate_monthly_interest_rate(annual_interest_rate):
    return annual_interest_rate / (12 * 100)

def calculate_annuity_payment(loan_principal, annual_interest_rate, total_payments):
    """
    Calculate the annuity payment for a loan.

    Args:
        loan_principal (float): The loan principal amount.
        annual_interest_rate (float): The annual interest rate as a percentage (e.g., 10 for 10%).
        total_payments (int): The total number of monthly payments.

    Returns:
        int: The annuity payment, rounded up to the nearest integer.
    """
    monthly_interest_rate = calculate_monthly_interest_rate(annual_interest_rate)
    annuity_payment = loan_principal * (
            monthly_interest_rate * math.pow(1 + monthly_interest_rate, total_payments)
    ) / (math.pow(1 + monthly_interest_rate, total_payments) - 1)
    return math.ceil(annuity_payment)


print(calculate_annuity_payment(1000000, 10, 60))

def calculate_loan_principal(annuity_payment, annual_interest_rate, total_payments):
    monthly_interest_rate = calculate_monthly_interest_rate(annual_interest_rate)
    principal =  annuity_payment / ((monthly_interest_rate * math.pow(1 + monthly_interest_rate,
                total_payments)) / (math.pow(1 + monthly_interest_rate, total_payments) - 1))
    return round(principal)

def calculate_number_of_payments(loan_principal, monthly_payment, annual_interest_rate):
    """
    Calculate the number of payments needed to repay a loan.

    Args:
        loan_principal (float): The loan principal amount.
        monthly_payment (float): The monthly payment (annuity payment).
        annual_interest_rate (float): The annual interest rate as a percentage (e.g., 10 for 10%).

    Returns:
        int: The total number of payments (rounded up to the nearest whole number).
    """
    # Convert annual interest rate to nominal monthly rate
    monthly_interest_rate = calculate_monthly_interest_rate(annual_interest_rate)

    # Calculate the number of payments
    numerator = math.log(monthly_payment / (monthly_payment - monthly_interest_rate * loan_principal))
    denominator = math.log(1 + monthly_interest_rate)
    total_payments = numerator / denominator

    # Return the number of payments, rounded up to the nearest integer
    return math.ceil(total_payments)


def display_menu():
    """
    Display the menu and get the user's choice.
    Returns:
        str: The user's choice ("m" or "p").
    """
    return input("""
    What do you want to calculate?
    Type "m" - for the number of monthly payments,
    Type "p" - for the monthly payment:
    """)

def convert_to_years_and_months(total_months):
    """
    Convert a total number of months into years and months.

    Args:
        total_months (int): The total number of months.

    Returns:
        tuple: A tuple containing the number of years and months (years, months).
    """
    years, months = divmod(total_months, 12)
    return years, months

def print_total_years_and_months(years, months):
    # Format the output
    if years > 0 and months > 0:
        print(f"It will take {years} years and {months} months to repay this loan!")
    elif years > 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {months} months to repay this loan!")

if args.principal and args.periods and args.interest and not args.payment:
    monthly_payments = calculate_annuity_payment(args.principal, args.interest, args.periods)
    print(f"Your monthly payment = {monthly_payments}!")
elif args.payment and args.periods and args.interest and not args.principal:
    principal = calculate_loan_principal(args.payment, args.interest, args.periods)
    print(f"Your loan principal = {principal}!")
elif args.principal and args.payment and args.interest and not args.periods:
    months_to_repay = calculate_number_of_payments(args.principal, args.payment, args.interest)
    years, months = convert_to_years_and_months(months_to_repay)
    print_total_years_and_months(years, months)
else:
    print("Insufficient arguments provided.")
