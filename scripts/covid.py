import pandas as pd
import geopandas
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df["Long"], df["Lat"]))

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.plot()
plt.show()

sj = geopandas.sjoin(gdf, world, how="left", op='intersects')

fig, ax = plt.subplots()
world.plot(ax=ax, color="white", edgecolor="black")
gdf.plot(ax=ax)
fig.show()

col = [c for c in sj.columns if '20' in c]

dfm = pd.melt(
    sj,
    id_vars = ["Province/State", "Country/Region", "continent", "Lat", "Long"],
    value_vars=col,
    var_name="Date",
    value_name="Cases"
)

gp = dfm.groupby("Country/Region", as_index=False)["Cases"].sum()
x = gp[gp["Cases"] >= 10000]

dfmf = dfm[dfm["Country/Region"].isin(x["Country/Region"])]

europa = dfmf[
    (dfmf["continent"].isin(["Europe"]))
    &
    (dfmf["Date"] >= '3/1/20')

]

fig = px.bar(
    europa,
    x="Country/Region",
    y="Cases",
    animation_frame="Date",
    animation_group="Country/Region",
    range_y=[0, 250000]
)

fig.layout.title = 'COVID-19'
fig.layout.sliders[0].pad.t = 150
fig.layout.updatemenus[0].pad.t = 150
fig.update_xaxes(categoryorder="max descending")

fig.show()