import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def open_file(fileName):
    data = pd.read_csv(fileName)
    return data

def method_equals_offense(data, method_index, weapon, crime_type):
    offense = data['offense'].value_counts()
    method = data['method'].value_counts()
    offense_keys = offense.keys()
    method_keys = method.keys()
    method_count = []

    for k in offense_keys:
        subset = data.loc[data['offense'] == k]
        count = subset.loc[subset['method'] == method_keys[method_index]]['method'].value_counts()
        method_count.append(count)

    sns.set_style("whitegrid")
    plt.ylabel("OFFENSES USING %s" % (weapon))
    plt.xlabel('OFFENSES')
    plt.title("%s EQUALS %s" % (weapon, crime_type))
    ax = sns.barplot(x=offense_keys, y=method_count)
    plt.show()

def day_equals_sex_abuse(data):
    shift = data['shift'].value_counts()
    offense = data['offense'].value_counts()
    shift_keys = shift.keys()
    offense_keys = offense.keys()
    shift_count = []

    for k in offense_keys:
        subset = data.loc[data['offense'] == k]
        count = subset.loc[subset['shift'] == shift_keys[2]]['shift'].value_counts()
        shift_count.append(count)

    sns.set_style("whitegrid")
    plt.ylabel("OFFENSES DURING THE DAY")
    plt.xlabel('OFFENSES')
    plt.title("DAY EQUALS SEX ABUSE")
    ax = sns.barplot(x=offense_keys, y=shift_count)
    plt.show()

def more_crimes_at_midnight(data):
    shift = data['shift'].value_counts()
    shift_keys = shift.keys()
    midnight_count = []

    for k in shift_keys:
        subset = data.loc[data['shift'] == k]
        count = subset['shift'].value_counts()
        midnight_count.append(count)

    sns.set_style("whitegrid")
    plt.ylabel("CRIMES PER SHIFT")
    plt.xlabel('SHIFT')
    plt.title("MORE CRIMES AT MIDNIGHT")
    ax = sns.barplot(x=shift_keys, y=midnight_count)
    plt.show()

if __name__ == '__main__':
    data = open_file("../resources/crime_with_cleaning.csv")
    #method_equals_offense(data, 1, 'GUNS', 'HOMICIDE')
    #method_equals_offense(data, 2, 'KNIFES', 'HOMICIDE')
    #method_equals_offense(data, 0, 'OTHERS', 'SEX ABUSE')
    #day_equals_sex_abuse(data)
    #more_crimes_at_midnight(data)
