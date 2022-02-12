import os
import random
import networkx as nx

import matplotlib.pyplot as plt

import plotly.graph_objects as go

import dash
import dash_cytoscape as cyto
import dash_core_components as dcc
import dash_html_components as html

NODES = ['Ava', 'Bob', 'Chi', 'Dev', 'Eve']
EDGES = [('Ava','Chi'), ('Bob','Dev'), ('Bob','Eve'), ('Chi', 'Eve')]

# https://networkx.org/documentation/stable/tutorial.html
G = nx.Graph()
G.add_node('Ava')
G.add_nodes_from(['Bob','Chi','Dev','Eve'])
G.add_edge('Ava', 'Eve')
G.add_edge(*('Ava','Bob'))
G.add_edges_from([('Ava','Chi'), ('Bob','Dev'), ('Bob','Eve'), ('Chi', 'Eve')])


app = dash.Dash()


'''
    https://plotly.com/python/network-graphs/
    Parameter examples:
        app = dash.Dash()
        elements = [
                    {'data': {'id': 'ca', 'label': 'Canada'}}, 
                    {'data': {'id': 'on', 'label': 'Ontario'}}, 
                    {'data': {'id': 'qc', 'label': 'Quebec'}},
                    {'data': {'source': 'ca', 'target': 'on'}}, 
                    {'data': {'source': 'ca', 'target': 'qc'}}
                ]
        description: <str>
        id='cytoscape'
        layout = {'name': 'breadthfirst'},
        style = {'width': '1024px', 'height': '1024px'}
'''
def graph_cytoscape(
    app,
    elements,
    description='Graph:',
    id='cytoscape',
    layout={'name': 'breadthfirst'},
    style={'width': '1024px', 'height': '1024px'}
    ):

    app.layout = html.Div([
        html.P(description),
        cyto.Cytoscape(
            id=id,
            elements=elements,
            layout=layout,
            style=style
        )
    ])

if __name__=='__main__':
    
    # nx.draw(G, with_labels=True)
    # plt.show()
    

    elements = []
    for node in NODES:
        elements.append({
            'data': {
                'id': node,
                'label': node
            }
        })
    for edge in EDGES:
        elements.append({
            'data': {
                'source': edge[0],
                'target': edge[1]
            }
        })
    
    for i in range(10):
        elements.append({
            'data': {
                'id': str(i),
                'label': str(i)
            }
        })
    for i in range(10):
        select = random.randint(0, 9)
        elements.append({
            'data': {
                'source': str(i),
                'target': str(select)
            }
        })

    graph_cytoscape(app, elements)
    app.run_server(debug=True, use_reloader=False)
    
    print('fin')
