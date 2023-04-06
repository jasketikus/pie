from math import pi

import pandas as pd

from bokeh.palettes import cividis
from bokeh.plotting import figure, show
from bokeh.transform import cumsum
from bokeh.embed import file_html
from bokeh.resources import CDN


def create_graph(**kwargs):

    x = kwargs

    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'country'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = cividis(len(x))

    p = figure(height=400, title="Characteristics", toolbar_location=None,
            tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='country', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None
  
    return file_html(p, CDN, "graph")