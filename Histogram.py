import plotly.express as px

def get_histogram_by_nlp_data(data: dict):
    new_dict = dict(POS=list(), count=list())
    for i in data.keys():
        new_dict['POS'].append(i)
        new_dict['count'].append(data[i][0])
    fig = px.histogram(new_dict, x='POS', y='count', labels={
        "POS": "POS",
        "count": "count in document",
    })
    fig.update_layout(yaxis_title="count in document")
    return fig.to_html()