import pandas as pd

goods_df = pd.read_csv(f"./PAD_03_PD.csv", sep=";")


## Zadanie 1
country_value_counts = goods_df['Country'].value_counts(dropna=False)
#print(country_value_counts)


## Zadanie 2
goods_df['owned_goods'] = goods_df[['owns_car', 'owns_TV', 'owns_house', 'owns_Phone']].sum(axis=1)
#print(goods_df)


## Zadanie 3
owned_goods_avg = goods_df[['gender', 'owned_goods']].groupby(['gender'], dropna=False).mean().round(2)
#print(owned_goods_avg)


## Zadanie 4
statistics = goods_df.groupby(['Country']).agg(owned_goods_avg=('owned_goods', 'mean'), age_min=('Age', 'min')).round({'owned_goods_avg': 2})
#print(statistics)