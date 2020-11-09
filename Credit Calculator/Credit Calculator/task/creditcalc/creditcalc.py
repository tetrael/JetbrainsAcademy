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
    overpayment = (payment * periods) - principal
    print("Your annuity payment = {0:n}!".format(payment))
    print("Overpayment = {0:n}".format(overpayment))


def annuity_principal(payment, periods, interest):
    nominal_interest_rate = (interest * 0.01) / 12
    principal = int(payment / (
        (nominal_interest_rate * pow(1 + nominal_interest_rate, periods)) /
        (pow(1 + nominal_interest_rate, periods) - 1)
    ))
    overpayment = (payment * periods) - principal
    print("Your credit principal = {0:n}!".format(principal))
    print("Overpayment = {0:n}".format(overpayment))


def annuity_periods(principal, payment, interest):
    nominal_interest_rate = (interest * 0.01) / 12
    periods = ceil(
        log(payment / (payment - nominal_interest_rate * principal),
            (1 + nominal_interest_rate)))
    years = periods // 12
    months = periods % 12
    overpayment = (payment * periods) - principal
    if years < 1:
        print("You need {0:n} months to repay this credit!".format(months))
        print("Overpayment = {0:n}".format(overpayment))
    elif months == 0 and years == 1:
        print("You need {0:n} year to repay this credit!".format(years))
        print("Overpayment = {0:n}".format(overpayment))
    elif months == 0:
        print("You need {0:n} years to repay this credit!".format(years))
        print("Overpayment = {0:n}".format(overpayment))
    else:
        print("You need {0:n} years and {1:n} months to repay this credit!".format(years, months))
        print("Overpayment = {0:n}".format(overpayment))


def diff_payment(principal, periods, interest):
    nominal_interest_rate = (interest * 0.01) / 12
    sum_of_payments = 0
    for month in range(1, periods+1):
        payment = ceil((principal / periods) + nominal_interest_rate *
                       (principal - ((principal * (month - 1)) / periods)))
        sum_of_payments += payment
        print("Month {0}: payment is {1}".format(month, int(payment)))
    overpayment = int(sum_of_payments - principal)
    print("\nOverpayment = {0}".format(overpayment))


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

if args.type == "diff" and args.interest:
    diff_payment(args.principal, args.periods, args.interest)
elif args.type == "annuity" and args.interest:
    if args.principal and args.periods and args.interest:
        annuity_payment(args.principal, args.periods, args.interest)
    elif args.payment and args.periods and args.interest:
        annuity_principal(args.payment, args.periods, args.interest)
    elif args.principal and args.payment and args.interest:
        annuity_periods(args.principal, args.payment, args.interest)
else:
    print("Incorrect parameters")
    quit()