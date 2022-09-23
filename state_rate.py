def state_rate(salary_input, state_input, status_input):
    import csv
    from collections import defaultdict

    columns = defaultdict(list)

    with open("State_Rates.csv", encoding="Latin-1") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for (k, v) in row.items():
                columns[k].append(v)

    f.close()

# This part of the code sorts each csv column into its own variable so that they can be easily split up into their own
# lists later.

    states = columns['State']
    rates_single = columns['Rates Single']
    brackets_single = columns['Brackets Single']
    rates_married = columns['Rates Married']
    brackets_married = columns['Brackets Married']

# This code ensures that the final element of each list is preserved when list is cleaned up of '' delimiters.

    list.append(rates_single, '')
    list.append(brackets_single, '')
    list.append(rates_married, '')
    list.append(brackets_married, '')

    try:
        while True:
            states.remove("")
    except ValueError:
        pass

# This code splits up each column into its own list.

    def list_split(base_list, sep_string):
        group = []
        for x in base_list:
            if x != sep_string:
                group.append(x)
            elif group:
                yield group
                group = []

    def list_convert(first_list):
        new_list = list(list_split(first_list, ''))
        return new_list

    split_rates_single = list_convert(rates_single)
    split_brackets_single = list_convert(brackets_single)
    split_rates_married = list_convert(rates_married)
    split_brackets_married = list_convert(brackets_married)

# Code for creating state dictionary that is used throughout rest of the program to access tax data related to the input
# state.

    state_index = states.index(state_input)
    state_dict = {'rate_single': split_rates_single[state_index], 'bracket_single': split_brackets_single[state_index],
                  'rate_married': split_rates_married[state_index],
                  'bracket_married': split_brackets_married[state_index]}

    rate_single = state_dict['rate_single']
    rate_married = state_dict['rate_married']

# Converts strings in list to floats as necessary
# In each converter, find way to detect whether it can be converted into a float
    def percent_convert(p):
        p = p.replace('%', '')
        p = p.replace('none', '0')
        p = float(p)
        p = p / 100
        return p

    def money_convert(m):
        m = m.replace('$', '')
        m = m.replace(',', '')
        m = m.replace('n.a.', '0')
        m = float(m)
        return m

    float_brackets = []

    if status_input == 1:
        for s in state_dict['bracket_single']:
            s = money_convert(s)
            float_brackets.append(s)
    elif status_input == 2:
        for s in state_dict['bracket_married']:
            s = money_convert(s)
            float_brackets.append(s)

    gross_salary = salary_input

# Finds user rate by comparing the input gross salary to each item in the brackets list, then creating a list of
# brackets less than the salary and a list of brackets greater than the salary. The index for the rate is taken from the
# final index of the lesser_than list.

    less_than, greater_than = [], []

    for b in float_brackets:
        if b < gross_salary:
            less_than.append(b)
        else:
            greater_than.append(b)

    rate_index = len(less_than) - 1

    if status_input == 1:
        user_rate = rate_single[rate_index]
    elif status_input == 2:
        user_rate = rate_married[rate_index]

# Calculates net salary.

    float_user_rate = percent_convert(user_rate)
    net_salary = gross_salary - (gross_salary * float_user_rate)

    return net_salary
