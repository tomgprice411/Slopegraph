import pandas as pd
import plotly.graph_objects as go




#import the dataset
df = pd.read_csv("Data.csv")

#convert date to datetime
df["TimePeriod"] = pd.to_datetime(df["TimePeriod"])

#######################
### Graph Variables ###
#######################

MARGIN = {"t": 50, "r": 40, "b": 40, "l": 40}
LINE_COLOUR = "#A6ACAF"
PRIMARY_COLOUR = "#1F618D"
FONT_COLOR = "#6d7578"
FONT_SIZE = 16
TITLE_COLOUR = "#303436"
TITLE_SIZE = 20
PLOTBG_COLOUR = "white"


#########################
### Create Slopegraph ###
#########################


#create an empty graph object called fig
fig = go.Figure()

#add a scatter plot graph to the object fig
fig.add_trace(go.Scatter(x = df["TimePeriod"], y = df["AOV"], marker = dict(color = PRIMARY_COLOUR)))

#customise the layout of the scatter plot
fig.update_layout(plot_bgcolor = PLOTBG_COLOUR, showlegend = False,
                    margin = MARGIN,
                    font = dict(color = FONT_COLOR, size = FONT_SIZE),
                    xaxis = dict(linecolor = LINE_COLOUR, tickformat = "%b-%Y", tickvals = ["2022-01-01", "2023-01-01"]),
                    yaxis = dict(visible = False, range = [0,80]),
                    title = dict(text = "AOV Increased by +£5 Between Jan 2023 and Jan 2022")
                    )


#add annotations to the scatter plot
for year, value in zip(df["TimePeriod"], df["AOV"]):
    if year == pd.to_datetime("2023-01-01"):
            fig.add_annotation(text = "  £{}".format(value),
                                xref = "x",
                                yref = "y",
                                x = year,
                                y = value,
                                align = "left",
                                xanchor = "left",
                                showarrow = False)

    elif year == pd.to_datetime("2022-01-01"):
        fig.add_annotation(text = "£{}  ".format(value),
                            xref = "x",
                            yref = "y",
                            x = year,
                            y = value,
                            align = "right",
                            xanchor = "right",
                            showarrow = False)

fig.show()



