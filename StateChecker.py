########################################################################################################################
#                                               MISSION STATEMENT                                                      #
########################################################################################################################
# This code is used for the development of the Income Tax Calculator. It checks the user's input for the standard two-
# letter abbrevation of a state's name. I aim to make this take as few lines of code as necessary by creating an dataset
# in the form of either a list or a dictionary so that the program can automatically match up any two standard abbrevi-
# ation to its matching full name.
#
# Author: Xander Leatherwood
#
# Contact: aleatherwood518@gmail.com
########################################################################################################################

import csv
from collections import defaultdict

# This section opens the State_Rates csv file in order to create a list of states (full names).

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

# Create a dictionary that assigns abbreviations to each entry in the list of states.

state_abbs = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS',
'MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND',"OH",'OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC']
state_dict = {}

# Only items with key-value pairs ("X":"Y") can be added to dictionaries. Therefore, a string must be created that takes the name of the
# state, its abbreviation, and then combines them into a key-value pair. 

for s in states:
    state_index = states.index(s)
    state_abb = state_abbs[state_index]
    state_dict.update({state_abb: s})

state_dict_keys = state_dict.keys()

state_check = None
while state_check is None:
    try:
        state_input = input("Enter your state (full name or two-letter postal abbreviation): ")
        if state_input in states:
            my_state = state_input
            break
        elif state_input in state_dict_keys:
            my_state = state_dict[state_input]
            break
    except ValueError:
        print("Invalid input!")

print(my_state)