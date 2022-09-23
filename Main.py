########################################################################################################################
#                                               MISSION STATEMENT                                                      #
########################################################################################################################
# This program is an income calculator that takes input salary on an hourly, weekly, bi-weekly, monthly, or yearly rate.
# Then, given input of the user's state of residence, it calculates the user's net income with local and federal income
# tax applied. This program assumes the user works year-round (ie not on a seasonal basis).
#
# Author: Xander Leatherwood
#
# Contact: aleatherwood518@gmail.com
########################################################################################################################

import federal_rate
import state_rate
import csv
from collections import defaultdict


def main():

    while True:

        # This section opens the State_Rates csv file in order to create a list of states that will be used later.

        columns = defaultdict(list)

        with open("State_Rates.csv", encoding="Latin-1") as f:
            reader = csv.DictReader(f)
            for row in reader:
                for (k, v) in row.items():
                    columns[k].append(v)

        f.close()

        states = columns['State']

        try:
            while True:
                states.remove("")
        except ValueError:
            pass

        # State abbreviation dictionary

        state_abbs = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS',
        'MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND',"OH",'OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC']
        state_dict = {}

        for s in states:
            state_index = states.index(s)
            state_abb = state_abbs[state_index]
            state_dict.update({state_abb: s})

        state_dict_keys = state_dict.keys()

        # This section of code takes user input for rate, wage, hours, state, marital status, and householder status.

        global rate_choice, hours_per_week, wage_per_rate, wage_adjustment_var
        print("Welcome to Xander's Yearly Net Wage Estimator!\n")
        print("To get started, choose whether to input your 1.) Hourly, 2.) Weekly, 3.) Bi-weekly, 4.) Monthly, or "
              "5.) Yearly salary:\n")
        check_rate = None
        while check_rate is None:
            try:
                rate_choice = int(input("1. Hourly \n2. Weekly \n3. Bi-Weekly \n4. Monthly \n5. Yearly\n"))
                if rate_choice < 1 or rate_choice > 5:
                    print("That wasn't an option, try again.")
                else:
                    break
            except ValueError:
                print("That wasn't an option, try again.")

        check_wage = None
        while check_wage is None:
            try:
                wage_per_rate = float(input("Enter your wage/salary in dollars ($): "))
                break
            except ValueError:
                print("Wrong input type, try again.")

        check_hours = None
        while check_hours is None:
            try:
                hours_per_week = float(input("Enter the number of hours worked per week: "))
                break
            except ValueError:
                print("Wrong input type, try again.")

        # There is probably a more efficient way of writing the code below. One idea is to create a dictionary that
        # assigns each state's full name to its two-letter initial. Could also be used to include other variants for the
        # name of each state (eg. Pennsylvania = "P.A.," "PA," "Penn.," "Penna.," etc.)

        check_state = None
        while check_state is None:
            try:
                state_input = str(input("Enter your state (full name or two-letter initial): "))
                
                state_cap = state_input.capitalize()
                state_upper = state_input.upper()

                if state_cap in states:
                    state = state_cap
                    break
                elif state_upper in state_dict_keys:
                    state = state_dict[state_upper]
                    break
                else:
                    print("Wrong input, try again.")
            except ValueError:
                print("Wrong input type, try again.")

        check_status = None
        while check_status is None:
            try:
                status = int(input("Enter your marital status:\n 1. Single\n 2. Married"))
                break
            except ValueError:
                print("Wrong input type, try again.")

        check_house = None
        while check_house is None:
            try:
                house = int(input("Are you the head of your household?\n 1. Yes\n 2. No"))
                break
            except ValueError:
                print("Wrong input type, try again.")

    # This section of code evaluates the user input wage rate and determines how to apply to final wage calculation.

        if rate_choice == 1:
            wage_adjustment_var = hours_per_week
        if rate_choice == 2:
            wage_adjustment_var = 1
        if rate_choice == 3:
            wage_adjustment_var = 0.5
        if rate_choice == 4:
            wage_adjustment_var = 0.2307692307692308
        if rate_choice == 5:
            wage_adjustment_var = 0.0192307692307692

    # Wage calculation.

        gross_pay = float(wage_per_rate * 52 * wage_adjustment_var)

        print("Your yearly gross wage is: $", "{:.2f}".format(gross_pay))

        fed_pay = federal_rate.federal_rate(gross_pay, status, house)

        print("Your yearly wage with federal tax taken into account is: $", "{:.2f}".format(fed_pay))

    # State calculation.

        state_pay = state_rate.state_rate(fed_pay, state, status)

        print("Your yearly wage with state tax taken into account is: $", "{:.2f}".format(state_pay))

        break


main()


while True:
    answer = str(input("Run again? y/n"))
    if answer not in ('y', 'n'):
        print("Wrong input, try again.")
        continue
    if answer == 'y':
        main()
    else:
        print("Thanks for stopping by!")
        break
