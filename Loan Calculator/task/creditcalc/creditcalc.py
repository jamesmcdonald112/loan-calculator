# write your code here
principal_loan = int(input("Enter the loan principal:"))

monthly_repayment = int(input("Enter the monthly payment:"))

time_in_months_to_repay = principal_loan // monthly_repayment;

print(f"It will take {time_in_months_to_repay} months to repay the loan")