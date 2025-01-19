import math

def calculate_months_to_repay(loan_amount, monthly_payment):
    """
    Calculate the total number of months to repay the loan.
    Args:
        loan_amount (int): The total loan amount.
        monthly_payment (int): The monthly repayment amount.
    Returns:
        str: A formatted message indicating the number of months.
    """
    total_months = math.ceil(loan_amount / monthly_payment)
    return f"It will take {total_months} months to repay the loan."

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

def get_monthly_payment():
    """
    Prompt the user to enter the monthly payment amount.
    Returns:
        int: The entered monthly payment.
    """
    return int(input("Enter the monthly payment: "))

def get_number_of_months():
    """
    Prompt the user to enter the number of months.
    Returns:
        int: The entered number of months.
    """
    return int(input("Enter the number of months: "))

def calculate_monthly_payment(loan_amount, repayment_months):
    """
    Calculate the rounded monthly repayment and the last payment.
    Args:
        loan_amount (int): The total loan amount.
        repayment_months (int): The total number of months for repayment.
    Returns:
        tuple: A tuple containing the monthly payment and the last payment.
    """
    payment = loan_amount / repayment_months
    rounded_payment = math.ceil(payment)
    last_payment = loan_amount - (repayment_months - 1) * rounded_payment
    return rounded_payment, last_payment

# Main execution logic
loan_amount = int(input("Enter the loan principal: "))
user_choice = display_menu()

if user_choice == 'm':
    monthly_payment = get_monthly_payment()
    print(calculate_months_to_repay(loan_amount, monthly_payment))
elif user_choice == 'p':
    repayment_months = get_number_of_months()
    monthly_payment, last_payment = calculate_monthly_payment(loan_amount, repayment_months)
    print(f"Your monthly payment = {monthly_payment} and the last payment = {last_payment}.")
else:
    print("Invalid choice, please try again.")