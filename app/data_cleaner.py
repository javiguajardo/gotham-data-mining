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

if __name__ == '__main__':
    data = open_file("../resources/crime_with_errors.csv")
    data = rename_columns(data)
    data = replace_year_values(data)
    print(data)
