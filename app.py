import pathlib

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils import titlebar

BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("data").resolve()

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__)
server=app.server
app.title = 'SFR Dashboard'
bar_colors = ['#F5CDA7', '#FAA381', '#C9DBBA', '#99C5B5', '#899E8B', '#60935D', '#706C61', '#DCDBA8']
# bar_colors[1] = 'crimson'
colors = {
    'background': '#eef0a1',
    'text': '#092859'
}

#data = pd.read_csv("C://Users//User//Documents//fullsample")

tab_e = pd.read_csv(DATA_PATH.joinpath("data.csv"), engine="python")
tab_r = pd.read_csv(DATA_PATH.joinpath("receipts.csv"), engine="python")
summary = pd.read_csv(DATA_PATH.joinpath("summary.csv"), engine="python")
summary2 = pd.read_csv(DATA_PATH.joinpath("summary2.csv"), engine="python")
break_down = pd.read_csv(DATA_PATH.joinpath("breakdown.csv"), engine="python")

# lang1_subs = data.LANG1_SUB_NAME.unique()
# school_type = data.SCHOOL_TYPE.unique()
# dist = data.DISTRICT_NAME.unique()
# paper_lst = ["LANG1_SUB_NAME", "LANG2_SUB_NAME", "LANG3_SUB_NAME",
#              "SUB1_SUB_NAME", "SUB2_SUB_NAME", "SUB3_SUB_NAME",
#              "SUB4_SUB_NAME", "SUB5_SUB_NAME"]

app.layout = html.Div(
    [
        html.Div(
            titlebar(app),
        ),
        html.Div(
            [

                html.Div(
                    [
                    dcc.Graph(
                            config={
                                'displaylogo': False,
                                'responsive': True},
                            figure=px.sunburst(
                                summary,
                                path=['Type', 'Section', 'Name'],
                                values='Values',
                                title="Summary of Fiscal Transactions 2017-18",
                                height=700,
                                width=700,
                                labels={
                                    "Name": "Name",
                                    "parent": "Classified under",
                                    "Values": "Amount in Rupees",
                                    "labels": "id",
                                },
                                color="Section",
                                #color_discrete_sequence=px.colors.sequential.Mint[3:],
                                color_discrete_sequence=px.colors.sequential.dense[1:],
                                #color="Section",
                                #color_discrete_sequence=px.colors.qualitative.Pastel,
                                # template="seaborn",
                                # color="Name",
                                # color_continuous_scale=px.colors.sequential.BuGn,
                                # range_color=[10,15],
                                # hover_data=None,
                                # maxdepth=2
                                # branchvalues="remainder",
                                # hoverinfo=None,
                                # hover_name='Values',
                                # hover_data={"Name": False, "Type":False, "Section":False}
                                # color="Unarmed",
                                # color_discrete_sequence=px.colors.qualitative.Pastel,
                                # maxdepth=-1,                        # set the sectors rendered. -1 will render all levels in the hierarchy
                                # color="Victim's age",
                                # color_continuous_scale=px.colors.sequential.BuGn,
                                # range_color=[10,100],

                                # branchvalues="total",               # or 'remainder'
                                # hover_name="Unarmed",
                                # # hover_data={'Unarmed': False},    # remove column name from tooltip  (Plotly version >= 4.8.0)
                                # title="7-year Breakdown of Deaths by Police",
                                # template='ggplot2',               # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
                                #                                   # 'plotly_white', 'plotly_dark', 'presentation',
                                #                                   # 'xgridoff', 'ygridoff', 'gridon', 'none',
                                #template='ggplot2'
                            ),
                        ),
                        html.Div(
                        [
                        html.P(
                            "This set of sunburst charts captures a snapshot of the finances of the Government of Karnataka during"
                            " 2017-18 and 2018-19. It analyses important changes in major fiscal indicators vis-à-vis the other."
                            " This Analysis is based on the finance accounts and information obtained from the Government of Karnataka."
                            " Click on the chart to explore further.",
                        ),
                        html.Li("Revenue receipts grew by 17,979.01 crore, about 12% compared to previous year"),
                        html.Li("Revenue expenditure increased by 21,817.53 crore, about 15%"),
                        html.Li("Capital outlay increased by 3,992.56 crore, about 13 per cent, increase was mainly under"
                         "Economic Services Sector (3,025.80 crore, 14 per cent) and Social Services Sector (1,116.80"
                         "crore, 13 per cent) and off-set by decrease under General Services Sector (150.04 crore, 15 per cent)"),
                        html.Li("Recoveries of Loans and Advances decreased by 105.70 crore (77 per cent) mainly due"
                         "to less recovery of loans under 7615-200-Miscellaneous Loans during 2018-19.  The"
                          "disbursement of Loans and Advances decreased by 605 crore (12 per cent)"),
                        ], style={
                                "padding": "30px"
                            }
                        )
                    ],
                    className="six columns card"
                ),
                html.Div(
                    [

                        dcc.Graph(
                            config={
                                'displaylogo': False,
                                'responsive': True
                            },
                            figure=px.sunburst(
                                summary2,
                                path=['Type', 'Section', 'Name'],
                                values='Values',
                                title="Summary of Fiscal Transactions 2018-19",
                                height=700,
                                width=700,
                                labels={
                                    "Name": "Name",
                                    "parent": "Classified under",
                                    "Values": "Amount in Rupees",
                                    "labels": "id",
                                },
                                #template="ggplot2",
                                color="Section",
                                color_discrete_sequence=px.colors.sequential.Brwnyl[1:],
                                #hover_name='Values',
                            ),
                        ),
                        html.Div(
                        [
                        html.Li("Public Account receipts increased by 37,144.56 crore (19 per cent) and"
                        " disbursements by 39,792.96 crore (20 per cent); and"),
                        html.Li("Public Debt receipts (excluding ways and means advances) increased by 16,792.20"
                         "crore (67 per cent) and repayments increased by 2,813.46 crore (34 per cent)."
                         "The increase in Public Debt receipts was mainly due to increase in Internal Debt of the State"
                          "by 75 per cent over the previous year"),
                        html.Li("Miscellaneous Capital Receipts decreased from 3.70 crore in 2017-18 to"
                        "-5.51 crore in 2018-19 due to retirement of capital/disinvestment of co-operative "
                        "societies/bank (3.29 crore) and refund of Earnest Money Deposit of 8.80 crore to Karnataka "
                        "Industrial Area Development Board (KIADB)"),
                        html.Li("Cash balance of the State Government decreased by 4,180.18 crore (16 per cent). "
                        "Though there is decrease in cash balance over the previous year, in view of high cash balance,"
                        " it is suggested that Government may consider utilising their existing balances before "
                        "resorting to fresh borrowings"),
                        ], style={
                                "padding": "30px"
                            }
                        )
                    ],
                    className="six columns card"
                )
            ], className="row",
        ),
        # Graph 1
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="eight columns card",
                    children=[
                        dcc.Dropdown(id="outlay",
                                     options=[{'label': i, 'value': i} for i in tab_e.columns[1:]],
                                     value=[tab_e.columns[1], tab_e.columns[2], tab_e.columns[3]],
                                     multi=True),
                        dcc.Checklist(id="year_list",
                                      options=[
                                          {'label': " " + i, 'value': i} for i in
                                          tab_e.iloc[0:, 0].unique()
                                      ],
                                      value=[tab_e.iloc[4, 0], tab_e.iloc[3, 0], tab_e.iloc[1, 0]],
                                      labelStyle={
                                          "display": "inline-block",
                                          "margin-right": "20px",
                                          "cursor": "pointer"}
                                      ),
                        dcc.Graph(id="year_vs_everything",
                                  config={
                                      'modeBarButtonsToRemove': ['lasso2d'],
                                      'displaylogo': False,
                                      # 'responsive': True
                                  },
                                  )
                    ],
                    style={"padding": 30}
                ),
                html.Div(
                    className="four columns card",
                    children=[
                        html.P(
                        "State had created the Gender budget cell(January 2007) and gender budgeting was introduced"
                         " in 2007-08. The trends in Gender budget outlay and expenditure, Budget outlay and expenditure "
                         "category A and category B schemes is shown in the chart 'comparison of expenditure over years'.",
                   ),
                    html.Li(
                           "The total expenditure during 2014-15 to 2018-19 is more than the outlay except during"
                          " 2014-15 and 2017-18.  The decreasing proportion of the outlay vis-a-vis total outlay from"
                          " 50 per cent in 2014-15 to 39 per cent in 2018-19 is a matter of concern."),
                    html.Li(
                           "There was hardly any change in the allocation of Category A schemes in all the four years."
                           "  In 2018-19, there was a decrease in allocation by 21 per cent when compared to the "
                           "previous year.  This was due to drastic reduction in allocation in schemes like Ashraya "
                           "Basava Vasathi, Stree Shakti, Sabala etc.  Though the allocation increased under "
                           "Category B, the increase was marginal (2%)")
                ],style={
                        'padding':30
                        }
                ),
            ]
        ),
        # span
        html.Br(),
        # text
        html.P(
            "We have receipts on side and we can see detailed granular analysis of receipts on the other side. "
            "On the right the figure contains chained callbacks where input in dropdown is being dynamically updated. ",
            style={
                'padding': "30px"
            }
        ),
        # row3
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="six columns card",
                    children=[
                        dcc.Dropdown(id="receipts",
                                     options=[{'label': i, 'value': i} for i in tab_r.columns[1:]],
                                     value=[tab_r.columns[1], tab_r.columns[2]],
                                     multi=True),
                        dcc.Checklist(id="year_list_r",
                                      options=[{'label': " " + i, 'value': i} for i in tab_r.iloc[0:, 0].unique()],
                                      value=[tab_r.iloc[4, 0], tab_r.iloc[3, 0]],
                                      labelStyle={
                                          "display": "inline-block",
                                          "margin-right": "20px",
                                          "cursor": "pointer"
                                      }
                                      ),
                        dcc.Graph(id="year_vs_receipts",
                                  config={
                                      'modeBarButtonsToRemove': ['lasso2d'],
                                      'displaylogo': False,
                                      # 'responsive': True
                                  }
                                  )
                    ],
                    style={"padding": 30}
                ),
                html.Div(
                    className="six columns card",
                    children=[
                        dcc.Dropdown(id="subradio",
                                     multi=True,
                                     ),
                        dcc.RadioItems(id="radio",
                                       options=[
                                           {'label': ' Capital Receipts', 'value': 'cap'},
                                           {'label': ' Revenue Receipts', 'value': 'rev'},
                                           {'label': ' Public Account Receipts(Net)', 'value': 'pub'}
                                       ],
                                       value='cap',
                                       labelStyle={
                                           "display": "inline-block",
                                           "margin-left": "20px",
                                           "cursor": "pointer"
                                       }
                                       ),
                        dcc.Graph(id="breakdown",
                                  config={
                                      'modeBarButtonsToRemove': ['lasso2d'],
                                      'displaylogo': False,
                                      # 'responsive': True
                                  }
                                  )
                    ], style={"padding": 30}
                )
            ]
        )
    ], className="subpage1"
)

tab_e.set_index('Year', inplace=True)
tab_r.set_index('Year', inplace=True)


@app.callback(dash.dependencies.Output("year_vs_everything", "figure"),
              [dash.dependencies.Input("outlay", "value"),
               dash.dependencies.Input("year_list", "value")])
def update_graph(olay, lst):
    if len(olay) <= 1:
        dat1 = [dict(x=lst,
                     y=tab_e.iloc[:][olay[0]],
                     type="bar",
                     name=olay[0])]
        dat2 = []
    else:
        dat1 = [dict(x=lst,
                     y=tab_e.iloc[:][olay[0]],
                     type="bar",
                     name=olay[0])]
        dat2 = [dict(x=lst,
                     y=tab_e.loc[lst, :].iloc[:][item],
                     type="bar",
                     marker=go.bar.Marker(
                         color=bar_colors[olay.index(item) - 1]
                     ),
                     name=item) for item in olay[1:]]
    return (
        {"data": dat1 + dat2,
         "layout": go.Layout(
             title="Comparison of Expenditure over years",
             xaxis={
                 'title': 'Years',
                 "showgrid": True,
                 "showticklabels": True
             },
             yaxis={
                 'title': 'Variables selected in dropdown',
                 "showgrid": True,
                 "showticklabels": True,
                 "tickformat": ",g"
             },
             legend=dict(
                 y=-0.2,
                 x=0.1,
                 orientation='h'
             )
         )
         }
    )


@app.callback(dash.dependencies.Output("year_vs_receipts", "figure"),
              [dash.dependencies.Input("receipts", "value"),
               dash.dependencies.Input("year_list_r", "value")])
def update_graph(rec, lst):
    if len(rec) <= 1:
        dat1 = [dict(x=lst,
                     y=tab_r.iloc[:][rec[0]],
                     type="bar",
                     mode="markers",
                     width=0.5,
                     name=rec[0])]
        dat2 = []
    else:
        dat1 = [dict(x=lst,
                     y=tab_r.iloc[:][rec[0]],
                     type="bar",
                     mode="markers",
                     name=rec[0])]
        dat2 = [dict(x=lst,
                     y=tab_r.loc[lst, :].iloc[:][item],
                     type="bar",
                     mode="markers",
                     marker=go.bar.Marker(
                         color=bar_colors[rec.index(item) - 1]
                     ),
                     name=item) for item in rec[1:]]
    return (
        {"data": dat1 + dat2,
         "layout": go.Layout(
             title="Comparison of Receipts over years",
             xaxis={
                 'title': 'Years',
                 "showgrid": True,
                 "showticklabels": True
             },
             yaxis={
                 'title': 'Variables selected in dropdown',
                 "showgrid": True,
                 "showticklabels": True,
                 "tickformat": ",g"
             },
             legend=dict(
                 y=-0.2,
                 x=0.1,
                 orientation='h'
             )
         )
         }
    )


@app.callback(
    dash.dependencies.Output('subradio', 'options'),
    [dash.dependencies.Input('radio', 'value')]
)
def update_date_dropdown(rdio):
    return [{'label': i, 'value': i} for i in break_down.columns[1:]]


@app.callback(
    dash.dependencies.Output('subradio', 'value'),
    [dash.dependencies.Input('subradio', 'options')]
)
def set_cities_value(available_options):
    return [available_options[0]['value']]


# print(break_down["Revenue Receipts"]),print(break_down.iloc[:,1])
# r = ["Revenue Receipts", "Central tax transfers", "State's Own revenue"]
# q = "Revenue Receipts"
# print(break_down[r[0]])
# print([q])
# print((len(r)))


@app.callback(dash.dependencies.Output("breakdown", "figure"),
              [dash.dependencies.Input("radio", "value"),
               dash.dependencies.Input("subradio", "value")])
def update_graph(rad, srad):
    print(rad, srad)
    if len(srad) <= 1:
        dat1 = [dict(
            x=break_down.iloc[:, 0],
            y=break_down[srad[0]],
            type="bar",
            mode="markers",
            name=srad[0]
        )]
        dat2 = []
    elif len(srad) > 1:
        dat1 = [dict(
            x=break_down.iloc[:, 0],
            y=break_down[srad[0]],
            type="bar",
            mode="markers",
            name=srad[0]
        )]
        dat2 = [dict(
            x=break_down.iloc[:, 0],
            y=break_down[srad[item]],
            type="bar",
            mode="markers",
            marker=go.bar.Marker(
                color=bar_colors[item - 1]
            ),
            # marker_color=bar_colors[item-1],
            name=srad[item]
        ) for item in range(len(srad))[1:]]

    return ({"data": dat1 + dat2,
             "layout": go.Layout(
                 title="Comparison of Receipts over years",
                 # plot_bgcolor='aliceblue',
                 # colorscale="anil",
                 xaxis={
                     'title': 'Years',
                     "showgrid": True,
                     "showticklabels": True
                 },
                 yaxis={
                     'title': 'Sub classification',
                     "showgrid": True,
                     "showticklabels": True,
                     "tickformat": ",g"
                 },
                 legend=dict(
                     y=-0.2,
                     x=0.1,
                     orientation='h'
                 )
             )
             })


if __name__ == '__main__':
    #app.run_server(debug=False)
    app.run_server(debug=True, port=8049)
