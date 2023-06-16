import pandas as pd


def load_transactions(file):

    transactions_dataframe = pd.read_csv(file, header=None)[0].str.split(" ")

    transactions = []

    for sale in transactions_dataframe.values:
        sale_record = []
        for product in sale:
            if product != '':
                sale_record.append(int(product))
        transactions.append(sale_record)

    return transactions


def transform_rules(rules_string, products_list):
    rules = []

    for rule in rules_string:
        lhs = []
        for lh in rule.lhs:
            lhs.append(products_list[lh])

        rhs = []
        for rh in rule.rhs:
            rhs.append(products_list[rh])

        lhs.sort()
        rhs.sort()

        rules.append({
            'lhs': lhs,
            'rhs': rhs,
            'confidence': rule.confidence,
            'support': rule.support,
        })

    return rules


def load_product_names(file):

    products_dataframe = pd.read_csv(file, header=None)[0].str.split(" ", 1)

    products = {}

    for product in products_dataframe.values:
        products[int(product[0])] = product[1].replace('"', '')

    return products
