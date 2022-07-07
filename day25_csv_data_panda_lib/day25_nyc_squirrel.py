import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(df[df['Primary Fur Color'] == "Gray"])
red_squirrels_count = len(df[df['Primary Fur Color'] == "Cinnamon"])
black_squirrels_count = len(df[df['Primary Fur Color'] == "Black"])


print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count" : [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df2 = pd.DataFrame(data_dict)
df2.to_csv("squirrel_count.csv")