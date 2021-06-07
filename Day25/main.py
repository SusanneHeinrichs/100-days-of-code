import pandas as pd 

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = len(df[df["Primary Fur Color"] == "Gray"])
red_squirrels = len(df[df["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(df[df["Primary Fur Color"] == "Black"])

squirrels_dict = {
    "colors" : ["Gray", "Red", "Black"],
    "Squirrel count" : [gray_squirrels, red_squirrels, black_squirrels]
}

squirrels_count = pd.DataFrame(squirrels_dict)
squirrels_count.to_csv("squirrels_count.csv")