import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
myretaildata = pd.read_excel('')
myretaildata['Description'] = myretaildata['Description'].str.strip()
myretaildata.dropna(axis=0, subset=['InvoiceNo'], inplace=True)
myretaildata['InvoiceNo'] = myretaildata['InvoiceNo'].astype('str')
myretaildata = myretaildata[~myretaildata['InvoiceNo'].str.contains('C')]
myretaildata['Country'].value_counts()
mybasket = (myretaildata[myretaildata['Country'] == "Germany"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))
def my_encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

my_basket_sets = mybasket.applymap(my_encode_units)
my_basket_sets.drop('POSTAGE', inplace=True, axis=1)
my_frequent_itemsets = apriori(my_basket_sets, min_support=0.07, use_colnames=True)
my_rules = association_rules(my_frequent_itemsets, metric="lift", min_threshold=1)
my_rules.head(100)