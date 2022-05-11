import pandas as pd

results = pd.read_csv('results.csv')
results["movie"] = results["movie_or_TV_name"]

resultcount = pd.DataFrame({'movie':results.groupby("movie").size().index, 'number of shared actors':results.groupby("movie").size().values})
top10 = resultcount.sort_values(["number of shared actors"], ascending = False)
top10[:10]

import plotly.express as px
fig = px.bar(top10[:100], x='movie', y='number of shared actors')
fig.show()