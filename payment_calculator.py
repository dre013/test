def main():
    print('This is a monthly payment loan calculator')

    principal = float(input('Input the loan amount: '))
    apr = float(input('Input the annual interest rate: '))
    years = int(input('Input amount of years: '))

    monthly_interest_rate = apr / 1200
    amount_of_month = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_month))

    print('The monthly payment for this loan is: $%.2f' % monthly_payment)

main()