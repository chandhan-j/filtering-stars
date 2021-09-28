import plotly.express as px
import csv
import pandas as pd

rows = []

with open("star_with_gravity.csv","r") as f:
  csvreader = csv.reader(f)
  
  for row in csvreader:
    rows.append(row)

df = pd.read_csv("star_with_gravity.csv")

headers = rows[0]
stars_data_rows = rows[1:]

fig = px.scatter(df, x=df["Distance"] , y=df["Gravity"])
fig.show()

good_gravity_stars = []

for i in stars_data_rows:
  if float(i[2]) <= 100:
    good_gravity_stars.append(i)

print(len(good_gravity_stars))

ideal_stars = []

for i in good_gravity_stars:
  if float(i[5]) > 150 and float(i[5] < 350):
    ideal_stars.append(i)

print(len(ideal_stars))


df = pd.DataFrame(ideal_stars)
df.to_csv("data.csv")