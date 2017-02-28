import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def open_file(fileName):
    data = pd.read_csv(fileName)
    return data

def gun_equals_homicide(data):
    offense = data['offense'].value_counts()
    method = data['method'].value_counts()
    offense_keys = offense.keys()
    method_keys = method.keys()
    guns_count = []


    for k in offense_keys:
        subset = data.loc[data['offense'] == k]
        count = subset.loc[subset['method'] == method_keys[1]]['method'].value_counts()
        guns_count.append(count)

    sns.set_style("whitegrid")
    plt.ylabel('OFFENSES WITH GUNS')
    plt.xlabel('OFFENSES')
    plt.title('GUNS EQUALS HOMICIDE')
    ax = sns.barplot(x=offense_keys, y=guns_count)
    plt.show()

if __name__ == '__main__':
    data = open_file("../resources/crime_with_cleaning.csv")
    gun_equals_homicide(data)
    print(data)
