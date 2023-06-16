import json
from efficient_apriori import apriori
from data_processor import load_transactions, load_product_names, transform_rules

support = 0.0001
confidence = 0.0007
sales_file = 'data/Sales1998.txt'
product_list_file = 'data/productList.txt'

transactions = load_transactions(sales_file)
_, rules = apriori(transactions=transactions,
                   min_support=support, min_confidence=confidence)

products_list = load_product_names(file=product_list_file)

transformed_rules = transform_rules(rules, products_list)

with open('data/results.json', 'w') as file:
    json.dump(transformed_rules, file, indent=4)
    print(transform_rules(rules, products_list))
    # print(rules)
    # print(transactions, rules, products_list)
