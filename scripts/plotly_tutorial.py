import plotly.express as px
import pandas as pd

iris = px.data.iris()

fig = px.scatter(iris, x="sepal_length", y="sepal_width")
fig.show()

fig = px.scatter(iris, x="sepal_length", y="sepal_width", color="species")
fig.show()


fig = px.scatter(
    iris, 
    x="sepal_length", 
    y="sepal_width", 
    color="species",
    trendline="ols"
)
fig.show()


fig = px.scatter_matrix(
    iris
)
fig.show()

fig = px.scatter_matrix(
    iris,
    dimensions=[
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
    ]
)
fig.show()


fig = px.scatter_matrix(
    iris,
    dimensions=[
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
    ],
    color="species"
)
fig.show()


fig = px.scatter(iris, x="sepal_length", y="sepal_width")
fig.data

type(fig.data)
type(fig.data[0])

fig.data[0].x

fig.add_trace(
    px.scatter(iris, x="petal_length", y="petal_width").data[0]
)


fig.data[0].marker.color = 'red'
fig.show()

fig.layout.title = 'Sepalo e Petalo di Iris'
fig.show()

fig.layout.xaxis.title.text = 'lunghezza sepalo e petalo (cm)'
fig.layout.yaxis.title.text = 'larghezza sepalo e petalo (cm)'
fig.show()

fig.data[0].showlegend = True
fig.data[1].showlegend = True
fig.show()

fig.data[0].name = 'Sepalo'
fig.data[1].name = 'Petalo'


box = px.box(iris, "species", "sepal_width")
box.show()


grouped = iris.groupby("species", as_index=False)["sepal_width"].mean()

bar = px.bar(grouped, "species", "sepal_width")
bar.show()

hist = px.histogram(iris, "species", "sepal_width", histfunc='avg')
hist.show()

fig = px.scatter(iris, "sepal_length", "sepal_width", facet_col="species")
fig.show()


pp = '/home/matteo/Desktop/python/data/prison_category.csv'

prigionieri = pd.read_csv(pp)

pr_hist = px.histogram(prigionieri, "Region", "Count", color="Category", histfunc="avg", facet_col="Category")
pr_hist.show()

pr_hist = px.histogram(
    prigionieri, 
    "Region", 
    "Count", 
    color="Category", 
    histfunc="avg", 
    facet_col="Category",
    animation_frame="Year"
)

pr_hist.show()