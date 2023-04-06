from bokeh.models import ColumnDataSource
from bokeh.palettes import Bright6
from bokeh.plotting import figure, show
from bokeh.transform import factor_cmap
from bokeh.embed import file_html
from bokeh.resources import CDN


def create_graph():
    fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
    counts = [5, 3, 4, 2, 4, 6]

    source = ColumnDataSource(data=dict(fruits=fruits, counts=counts))

    p = figure(x_range=fruits, height=350, toolbar_location=None, title="Fruit Counts")

    p.vbar(x='fruits', top='counts', width=0.9, source=source, legend_field="fruits",
        line_color='white', fill_color=factor_cmap('fruits', palette=Bright6, factors=fruits))

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.y_range.end = 9
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    return file_html(p, CDN, "graph")