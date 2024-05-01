import csv
import re
import pandas as pd
import os


def exporting_data():
    if os.path.isfile('x_calendar_data.csv'):
        os.remove('x_calendar_data.csv')
        pass
    if not os.path.isfile('x_calendar_data.csv'):
        html = 'https://www.premierleague.com/tables'
        table = pd.read_html(html)
        table[0].to_csv('x_calendar_data.csv')


def arr_data():
    with (open('x_calendar_data.csv', 'r') as arranger):
        r = csv.reader(arranger)
        dic = []
        for line in r:
            d = {}
            club_pattern = r'[A-Z]{3}'
            hour_pattern = r'[0-9][0-9]:[0-5][0-9]'
            date_pattern = r'\w+ [0-9]+ \w+ [0-9]+'
            match_name = re.findall(club_pattern, line[12])
            match_hour = re.findall(hour_pattern, line[12])
            match_date = re.findall(date_pattern, line[12])
            if len(match_name) == 4 and len(match_date) == 1:
                d['home'] = match_name[2]
                d['away'] = match_name[3]
                d['date'] = ' '.join(match_date)
                d['time'] = ' '.join(match_hour)
            if len(match_name) == 2 and len(match_date) == 1:
                d['home'] = match_name[0]
                d['away'] = match_name[1]
                d['date'] = ' '.join(match_date)
                d['time'] = ' '.join(match_hour)
            dic.append(d)
            for item in dic:
                if item == {}:
                    dic.remove(item)
        result = pd.DataFrame(dic)
        result.to_csv('PL_nxt_match.csv')
        # ----------------sorting data--------------#
        with open('PL_nxt_match.csv', 'r') as read:
            l = read.readlines()
            result0 = sorted(l, key=lambda x: re.findall(r'( [0-9] )|([0-9][0-9]:[0-9][0-9])', x))
            txt = ' '.join(result0)
        if os.path.isfile('t.txt'):
            os.remove('t.txt')
            pass
        if not os.path.isfile('t.txt'):
            with open('t.txt', 'w+') as t:
                pattern = r'[^0-9][0-9]{1,2},'
                dup_rem_pattern = r'(\w+,\w+,\w+ [0-9]+ \w+ [0-9]+,[0-9]+:[0-9]+)(?![\s\S]*\1)'
                match = re.sub(pattern, '', txt)
                match = re.sub(r'^,', '', match)
                match1 = re.sub(dup_rem_pattern, '', match)

                t.write(match1)
            c = pd.read_csv('t.txt')
            c.to_excel('PL_match_dates.xlsx')
            print(c)
            os.remove('t.txt')
            os.remove('PL_nxt_match.csv')
