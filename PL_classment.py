import csv
import pandas as pd
import os


def file_exist():
    #os.chdir('premier_league')
    if os.path.isfile('x_classment_data.csv'):
        os.remove('x_classment_data.csv')
        pass
    if not os.path.isfile('x_classment_data.csv'):
        html = 'https://www.lequipe.fr/Football/championnat-d-angleterre/page-classement-equipes/general'
        table = pd.read_html(html)
        table[0].to_csv('x_classment_data.csv')


def data_arrng():
    with open('x_classment_data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        data_dict = []
        x = 0
        for row in reader:
            d = {'classment': str(x), 'Club': row[2], 'Points': row[4], 'Win': row[6], 'Null': row[7], 'Loss': row[8]}
            data_dict.append(d)
            x += 1
        # creating a new dataframe
        result = pd.DataFrame(data_dict[1:])
        with pd.ExcelWriter('PL_classment.xlsx') as writer:
            result.to_excel(writer, index=False)
    print(pd.read_excel('PL_classment.xlsx', index_col=0))