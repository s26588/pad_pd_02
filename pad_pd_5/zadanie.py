import numpy as np
import pandas as pd

orders_df = pd.read_csv(f"./orders.csv", sep=",")
customers_df = pd.read_csv(f"./customers.csv", sep=",")

### Zadanie 1

print(orders_df.describe())
print()
print(orders_df.info())
print()
print(orders_df.head())

## a)
orders_df['order_date'] = pd.to_datetime(orders_df['order_date'], format="%Y-%m-%d")
#print(orders_df)

## b)
print(f"Liczba wartości w kolumnie 'tshirt_category': {len(orders_df['tshirt_category'])}")
print(f"Liczba unikalnych wartości w kolumnie 'tshirt_category': {len(orders_df['tshirt_category'].unique())}")
print(f"Unikalne wartości {orders_df['tshirt_category'].unique()}")

## c)
def clean_cat(category):
    category = category.lower()
    category = category.replace("wh ", "white ").replace("bl ", "black ")
    category = category.replace("tshirt", "t-shirt").replace("tennis shirt", "t-shirt")

    return category

orders_df['tshirt_category'] = orders_df['tshirt_category'].apply(clean_cat)
print(f"Unikalne wartości {orders_df['tshirt_category'].unique()}")

## d)
def get_colour(category):
    splitted_category = category.split()
    if len(splitted_category) == 1:
        return None

    return splitted_category[0]

def get_type(category):
    splitted_category = category.split()
    if len(splitted_category) == 1:
        return category

    return splitted_category[1]

def get_gender(category):
    splitted_category = category.split()
    if len(splitted_category) == 1:
        return None

    return splitted_category[2]

def split_cat(category):
    splitted_category = category.split()
    if len(splitted_category) == 1:
        splitted_category.insert(0, None)
        splitted_category.insert(2, None)

    return splitted_category


orders_df['tshirt_colour'] = orders_df['tshirt_category'].apply(get_colour)
orders_df['tshirt_type'] = orders_df['tshirt_category'].apply(get_type)
orders_df['tshirt_gender'] = orders_df['tshirt_category'].apply(get_gender)

# print(orders_df)

## e)
print(orders_df[(orders_df['order_date'] >= '2014-12-31') & (orders_df['order_date'] <= '2016-08-02')])


### Zadanie 2

## a)
print(customers_df.columns);

## b)
print(customers_df.shape)
print(orders_df.shape)

## c)
customers_df.rename(columns={'customerID': 'customer_id'}, inplace=True)

## d)
purchase_df = orders_df.merge(customers_df, how='left', on='customer_id')
print(purchase_df);


### Zadanie 3

purchase_df.to_csv("purchase.csv", index=False, sep=",")
