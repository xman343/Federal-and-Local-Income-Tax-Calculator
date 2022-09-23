def federal_rate(gross_pay, status, house):
    import csv

    data = []

    with open("Fed_Rates.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    disallowed_characters = "$,"

    if house == 1:
        str_bracket_01 = data[2][3]
        str_bracket_02 = data[3][3]
        str_bracket_03 = data[4][3]
        str_bracket_04 = data[5][3]
        str_bracket_05 = data[6][3]
        str_bracket_06 = data[7][3]
    if house == 2:
        if status == 1:
            str_bracket_01 = data[2][1]
            str_bracket_02 = data[3][1]
            str_bracket_03 = data[4][1]
            str_bracket_04 = data[5][1]
            str_bracket_05 = data[6][1]
            str_bracket_06 = data[7][1]
        elif status == 2:
            str_bracket_01 = data[2][2]
            str_bracket_02 = data[3][2]
            str_bracket_03 = data[4][2]
            str_bracket_04 = data[5][2]
            str_bracket_05 = data[6][2]
            str_bracket_06 = data[7][2]

    for character in disallowed_characters:
        str_bracket_01 = str_bracket_01.replace(character, "")
        str_bracket_02 = str_bracket_02.replace(character, "")
        str_bracket_03 = str_bracket_03.replace(character, "")
        str_bracket_04 = str_bracket_04.replace(character, "")
        str_bracket_05 = str_bracket_05.replace(character, "")
        str_bracket_06 = str_bracket_06.replace(character, "")

    bracket_one = float(str_bracket_01)
    bracket_two = float(str_bracket_02)
    bracket_three = float(str_bracket_03)
    bracket_four = float(str_bracket_04)
    bracket_five = float(str_bracket_05)
    bracket_six = float(str_bracket_06)

    if gross_pay <= bracket_one:
        fed_rate = 0.1
    if bracket_one < gross_pay <= bracket_two:
        fed_rate = 0.12
    if bracket_two < gross_pay <= bracket_three:
        fed_rate = 0.22
    if bracket_three < gross_pay <= bracket_four:
        fed_rate = 0.24
    if bracket_four < gross_pay <= bracket_five:
        fed_rate = 0.32
    if bracket_five < gross_pay <= bracket_six:
        fed_rate = 0.35
    if gross_pay > bracket_six:
        fed_rate = 0.37

    fed_pay = gross_pay - (gross_pay * fed_rate)
    return fed_pay
