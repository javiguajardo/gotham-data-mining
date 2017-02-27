import pandas as pd
import matplotlib.pyplot as plt

def open_file(fileName):
    data = pd.read_csv(fileName)
    return data

def rename_columns(data):
    data = data.rename(columns={'mont': 'month', 'REPORT_DAT': 'report_date',
    'SHIFT': 'shift', 'OFFENSE': 'offense', 'METHOD': 'method',
    'DISTRICT': 'district'})

    return data

def replace_year_values(data):
    report_date = data['report_date']
    year = data['year']
    report_date_years = []

    for rd in report_date:
        report_date_year = int(rd.split('/')[2])
        report_date_years.append(report_date_year)

    for i, y in enumerate(year):
        if(y != report_date_years[i]):
            data.loc[i, 'year'] = report_date_years[i]

    return data

def replace_month_values(data):
    month = data['month']

    for i, m in enumerate(month):
        if m == 'ENE':
            data.loc[i, 'month'] = 1
        elif m == 'FEB':
            data.loc[i, 'month'] = 2
        elif m == 'MAR':
            data.loc[i, 'month'] = 3
        elif m == 'ABR':
            data.loc[i, 'month'] = 4
        elif m == 'MAY':
            data.loc[i, 'month'] = 5
        elif m == 'JUN':
             data.loc[i, 'month'] = 6
        elif m == 'JUL':
            data.loc[i, 'month'] = 7
        elif m == 'AGO':
            data.loc[i, 'month'] = 8
        elif m == 'SEP':
            data.loc[i, 'month'] = 9
        elif m == 'OCT':
            data.loc[i, 'month'] = 10
        elif m == 'NOV':
            data.loc[i, 'month'] = 11
        elif m == 'DIC':
            data.loc[i, 'month'] = 12

    return data

def lower_to_uppercase(data, attribute):
    records = data[attribute]

    for i, r in enumerate(records):
        if r.islower():
            data.loc[i, attribute] = r.upper()

    return data

def letter_to_word(data, attribute):
    records = data[attribute]
    shift_values = {
        'day': 'DAY',
        'evening': 'EVENING',
        'midnight': 'MIDNIGHT'
    }
    offense_values = {
        'homicide': 'HOMICIDE',
        'sex_abuse': 'SEX ABUSE'
    }
    method_values = {
        'knife': 'KNIFE',
        'gun': 'GUN',
        'other': 'OTHERS'
    }

    for i, r in enumerate(records):
        if attribute == 'shift':
            if r == 'D':
                data.loc[i, attribute] = shift_values['day']
            elif r == 'E':
                data.loc[i, attribute] = shift_values['evening']
            elif r == 'M':
                data.loc[i, attribute] = shift_values['midnight']
        elif attribute == 'offense':
            if r == 'H':
                data.loc[i, attribute] = offense_values['homicide']
            elif r == 'S':
                data.loc[i, attribute] = offense_values['sex_abuse']
        elif attribute == 'method':
            if r == 'K':
                data.loc[i, attribute] = method_values['knife']
            elif r == 'G':
                data.loc[i, attribute] = method_values['gun']
            elif r == 'O':
                data.loc[i, attribute] = method_values['other']

    return data

def fill_offense_values_with_mean(data):
    offenses = data['offense']
    offense_values = offenses.values
    max_offense = offense_values.max()

    for i, o in enumerate(offenses):
        if o == '?':
            data.loc[i, 'offense'] = max_offense

    return data

if __name__ == '__main__':
    data = open_file("../resources/crime_with_errors.csv")
    data = rename_columns(data)
    data = replace_year_values(data)
    data = replace_month_values(data)
    data = lower_to_uppercase(data, 'shift')
    data = lower_to_uppercase(data, 'offense')
    data = letter_to_word(data, 'shift')
    data = letter_to_word(data, 'offense')
    data = letter_to_word(data, 'method')
    fill_offense_values_with_mean(data)
    print(data)
