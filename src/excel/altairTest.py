# import pandas as pd
from vega_datasets import data
import altair as alt

# data = pd.DataFrame({'country_id': [1, 2, 3, 4, 5, 6],'population': [1, 100, 200, 300, 400, 500],'income':[1000, 50, 200, 300, 200, 150]})
# categorical_chart = alt.Chart(data).mark_circle(size=200).encode(
#                         x='population:Q',
#                         y='income:Q',
#                         color='country_id:N')
cars = data.cars()

# chart = alt.Chart(cars).mark_point().encode(
#     x='Horsepower',
#     y='Miles_per_Gallon',
#     color='Origin',
# )

brush = alt.selection(type='interval')

points = alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color=alt.condition(brush, 'Origin', alt.value('lightgray'))
).add_selection(
    brush
)

bars = alt.Chart(cars).mark_bar().encode(
    y='Origin',
    color='Origin',
    x='count(Origin)'
).transform_filter(
    brush
)

chart = points & bars
alt.Chart.serve(chart)
