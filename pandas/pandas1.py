import pandas
food_info = pandas.read_csv("food_info.csv")
#print(type(food_info))
#print(food_info.dtypes)

#print(food_info.head(1))

# print(food_info.tail(4))
# print(food_info.columns)
# print(food_info.shape)

# print(food_info.loc[6])

# print(food_info.loc[3:6])

# print(food_info['NDB_No'])

columns = ['Zinc_(mg)', 'Copper_(mg)']
zinc_copper = food_info[columns]
#print(zinc_copper)

col_names = food_info.columns.tolist()
print(col_names)

gram_columns = []

for c in col_names:
    if c.endswith("(g)"):
        gram_columns.append(c)
gram_df = food_info[gram_columns]
print(gram_df.head(3))

