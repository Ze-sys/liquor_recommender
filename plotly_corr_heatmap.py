import plotly.figure_factory as ff
import plotly.express as px
import numpy as np
def plotly_corr_heatmap(df):
    '''
    Takes a data frame
    Returns corr heatmaps using plotly 
    '''
    corr = df.corr().round(2)
    mask = np.triu(np.ones_like(corr, dtype=bool))
    df_mask = corr.mask(mask)
    fig = ff.create_annotated_heatmap(z=df_mask.to_numpy(), 
                                    x=df_mask.columns.tolist(),
                                    y=df_mask.columns.tolist(),
                                    colorscale=px.colors.diverging.RdBu,
                                    showscale=True, ygap=1, xgap=1
                                    )
    fig.update_layout(
        font_size=16,
        title ='Correlations',
        margin = dict(l=0,r=0,b=0,t=60),
        coloraxis_colorbar_x=.7,
        width=800, 
        height=600,
        xaxis_showgrid=False,
        yaxis_showgrid=False,
        xaxis_zeroline=False,
        yaxis_zeroline=False,
        yaxis_autorange='reversed',
        paper_bgcolor = 'rgba(0,0,0,0)', #'aliceblue',
        plot_bgcolor='rgba(0,0,0,0)'
        )
    for i in range(len(fig.layout.annotations)):
        if fig.layout.annotations[i].text == 'nan':
            fig.layout.annotations[i].text = ""

    fig.update_xaxes(side="bottom")

    return fig