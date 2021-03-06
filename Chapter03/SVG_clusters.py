import plotly as py
import plotly.graph_objs as go
import numpy as np

# ----------pre def
pyplt = py.offline.plot


x0 = np.random.normal(2, 0.45, 300)
y0 = np.random.normal(2, 0.45, 300)

x1 = np.random.normal(6, 0.4, 200)
y1 = np.random.normal(6, 0.4, 200)

x2 = np.random.normal(4, 0.3, 200)
y2 = np.random.normal(4, 0.3, 200)

trace0 = go.Scatter(
    x=x0,
    y=y0,
    mode='markers',
)
trace1 = go.Scatter(
    x=x1,
    y=y1,
    mode='markers'
)
trace2 = go.Scatter(
    x=x2,
    y=y2,
    mode='markers'
)
trace3 = go.Scatter(
    x=x1,
    y=y0,
    mode='markers'
)
layout = {
    'shapes': [
        {
            'type': 'circle',
            'xref': 'x',
            'yref': 'y',
            'x0': min(x0),
            'y0': min(y0),
            'x1': max(x0),
            'y1': max(y0),
            'opacity': 0.2,
            'fillcolor': 'blue',
            'line': {
                'color': 'blue',
            },
        },
        {
            'type': 'circle',
            'xref': 'x',
            'yref': 'y',
            'x0': min(x1),
            'y0': min(y1),
            'x1': max(x1),
            'y1': max(y1),
            'opacity': 0.2,
            'fillcolor': 'orange',
            'line': {
                'color': 'orange',
            },
        },
        {
            'type': 'circle',
            'xref': 'x',
            'yref': 'y',
            'x0': min(x2),
            'y0': min(y2),
            'x1': max(x2),
            'y1': max(y2),
            'opacity': 0.2,
            'fillcolor': 'green',
            'line': {
                'color': 'green',
            },
        },
        {
            'type': 'circle',
            'xref': 'x',
            'yref': 'y',
            'x0': min(x1),
            'y0': min(y0),
            'x1': max(x1),
            'y1': max(y0),
            'opacity': 0.2,
            'fillcolor': 'red',
            'line': {
                'color': 'red',
            },
        },
    ],
    'showlegend': False,
}
data = [trace0, trace1, trace2, trace3]
fig = {
    'data': data,
    'layout': layout,
}

pyplt(fig, filename='tmp/clusters.html')
