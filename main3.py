import pandas as pd
import os

def count_items(census_data, criteria_list):

    df = census_data.copy()
    for attr, value in criteria_list:
        df = df[df[attr] == (attr + "=" + value)]

    return df.shape[0]


def pars_input(rule: str):
    rule_sides = rule.split('=>')
    X_list = []
    Y_list = []

    rule_left = rule_sides[0].replace('{', '')
    rule_left = rule_left.replace('}', '')

    rule_left_list = rule_left.split(',')
    for item in rule_left_list:
        item_list = item.split('=')
        X_list.append((item_list[0], item_list[1]))

    rule_right = rule_sides[1].replace('{', '')
    rule_right = rule_right.replace('}', '')

    rule_right_list = rule_right.split(',')
    for item in rule_right_list:
        item_list = item.split('=')
        Y_list.append((item_list[0], item_list[1]))

    return X_list, X_list + Y_list





def arrangingRules(rules):
    header_list = ['age', 'sex', 'education', 'native-country', 'race', 'marital-status', 'workclass', 'occupation',
                   'hours-per-week', 'income', 'capital-gain', 'capital-loss']
    census_data = pd.read_csv("census.csv", names=header_list)
    tups = []
    for rule in rules[1:]:
        X, Y = pars_input(rule)
        count_X = count_items(census_data, X)
        count_Y = count_items(census_data, Y)
        confidence = float(count_Y / count_X)
        tups.append((rule, confidence))

    tups.sort(key=lambda x: x[1])
    result = []
    for tup in tups:
        print(tup[1])
        result.append(tup[0])
    return result[::-1]




input_list = [3,
              '{native-country=United-States,capital-gain=None}=>{capital-loss=None}',
              '{capital-gain=None,capital-loss=None}=>{native-country=United-States}',
              'native-country=United-States,capital-loss=None}=>{capital-gain=None}']

print(arrangingRules(input_list))


v = 9



