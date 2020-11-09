# credit_principal = 'Credit principal: 1000'
# final_output = 'The credit has been repaid!'
# first_month = 'Month 1: paid out 250'
# second_month = 'Month 2: paid out 250'
# third_month = 'Month 3: paid out 500'

# write your code here
# print(credit_principal)
# print(first_month)
# print(second_month)
# print(third_month)
# print(final_output)

from math import ceil
from math import log
import sys
import argparse


def annuity_payment(principal, periods, interest):
    nominal_interest_rate = (interest * 0.01) / 12
    payment = ceil(principal * (
            (nominal_interest_rate * pow(1 + nominal_interest_rate, periods)) /
            (pow(1 + nominal_interest_rate, periods) - 1))
    )
    print(f'Your annuity payment = {payment}!')


args = sys.argv
if len(args) != 5:
    print("Incorrect parameters")
    quit()

parser = argparse.ArgumentParser("Loan calculator.")
parser.add_argument("--type", type=str, help="Indicates the type of payment: 'annuity' or 'diff' (differentiated)")
parser.add_argument("--payment", type=int, help="Is the monthly payment amount.")
parser.add_argument("--principal", type=int, help="Is used for calculations of both types of payment. "
                                                  "You can get its value if you know the interest, annuity payment, "
                                                  "and number of months.")
parser.add_argument("--periods", type=int, help="Denotes the number of months needed to repay the loan. "
                                                "It's calculated based on the interest, annuity payment, "
                                                "and principal.")
parser.add_argument("--interest", type=float, help="Is specified without a percent sign.")
args = parser.parse_args()

if args.type == "diff":
    pass
elif args.type == "annuity":
    annuity_payment(args.principal, args.periods, args.interest)

# if args.interest != '' and args.interest < 0:
#     print('Incorrect parameters')
# elif args.payment != '' and args.payment < 0:
#     print('Incorrect parameters')
# elif args.principal != '' and args.principal < 0:
#     print('Incorrect parameters')
# elif args.periods != '' and args.periods < 0:
#     print('Incorrect parameters')

# print('What do you want to calculate?')
# print('type "n" - for count of months,')
# print('type "a" - for annuity payment')
# print('type "p" - for monthly payment:')
# payment_type = input()

# if payment_type == 'n':
#     print('Enter the credit principal:')
#     credit_principal = int(input())
#     print('Enter monthly payment:')
#     monthly_payment = int(input())
#     print('Enter credit interest:')
#     credit_interest = float(input()) * 0.01
#     nominal_interest_rate = credit_interest / 12
#     count_of_periods = ceil(
#         log(monthly_payment / (monthly_payment - nominal_interest_rate * credit_principal),
#             (1 + nominal_interest_rate)))
#     years = count_of_periods // 12
#     months = count_of_periods % 12
#     if years < 1:
#         print(f'You need {months} months to repay this credit!')
#     elif months == 0 and years == 1:
#         print(f'You need {years} year to repay this credit!')
#     elif months == 0:
#         print(f'You need {years} years to repay this credit!')
#     else:
#         print(f'You need {years} years and {months} months to repay this credit!')
#
# elif payment_type == 'a':
#     print('Enter the credit principal:')
#     credit_principal = int(input())
#     print('Enter count of periods:')
#     counts_of_periods = int(input())
#     print('Enter credit interest:')
#     credit_interest = float(input()) * 0.01
#     nominal_interest_rate = credit_interest / 12
#     annuity_payment = ceil(credit_principal * (
#             (nominal_interest_rate * pow(1 + nominal_interest_rate, counts_of_periods)) /
#             (pow(1 + nominal_interest_rate, counts_of_periods) - 1))
#     )
#     print(f'Your annuity payment = {annuity_payment}!')
#
# elif payment_type == 'p':
#     print('Enter monthly payment:')
#     monthly_payment = float(input())
#     print('Enter count of periods:')
#     counts_of_periods = int(input())
#     print('Enter credit interest:')
#     credit_interest = float(input()) * 0.01
#     nominal_interest_rate = credit_interest / 12
#     credit_principal = monthly_payment / (
#         (nominal_interest_rate * pow(1 + nominal_interest_rate, counts_of_periods)) /
#         (pow(1 + nominal_interest_rate, counts_of_periods) - 1)
#     )
#     print(f'Your credit principal = {credit_principal}!')
