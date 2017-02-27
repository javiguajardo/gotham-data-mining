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
    print(f"{attribute}")

    for i, r in enumerate(records):
        if r.islower():
            r = r.upper()
            data.loc[i, attribute] = r

    return data

if __name__ == '__main__':
    data = open_file("../resources/crime_with_errors.csv")
    data = rename_columns(data)
    data = replace_year_values(data)
    data = replace_month_values(data)
    data = lower_to_uppercase(data, 'shift')
    data = lower_to_uppercase(data, 'offense')
    print(data)
