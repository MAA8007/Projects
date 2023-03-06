import imp
from posixpath import split
import csv
import pandas

gray = 0
red = 0
cinnamon = 0

data = pandas.read_csv("Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Furcolor_list = data["Primary Fur Color"]
print(Furcolor_list)
for x in Furcolor_list:
    if x == "Gray":
        gray +=1
    elif x == "Red":
        red +=1
    elif x == "Cinnamon":
        cinnamon+=1

data_dict = {"colours":["gray","red","cinnamon"],"number":[gray, red, cinnamon]}
data = pandas.DataFrame(data_dict)
data.to_csv("Day25/Colors.csv")
