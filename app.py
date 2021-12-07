import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.title('QS Ranking')

df = pd.read_csv(r'./ranking.csv', index_col=0)
top_n = int(st.number_input(label='Show Top n rows:', min_value=10))

st.dataframe(df.head(top_n))

st.write('-----')
st.write("Countries with the most top universities in the world")
df2 = pd.DataFrame(columns=['Country'])
df2['Country'] = df["City, Country"].apply(lambda x: x.split(",")[-1])
st.dataframe(df2['Country'].value_counts())
# st.write(df2['Country'].value_counts)

st.write('-----')
st.write('Historical Rankings of Top 25 Universities')
df3 = df.copy()
df3 = df3.head(25)
df3 = df3[['Current Ranking', '2021 Ranking', '2020 Ranking', '2019 Ranking','University Name']]
df3 = df3[df3.columns[::-1]]

st.dataframe(df3)



df3['Current Ranking'] = df3['Current Ranking'].apply(lambda x: x.replace('=', ''))
years = [2019, 2020, 2021, 2022]
rank = np.arange(1,26)

uni_to_plot = st.selectbox("Plot historical Ranking of:", df3['University Name'].to_list())
ranking_dict = dict(zip(df3['University Name'], df3.index))

fig = go.Figure(
    data=[go.Scatter(x=years, y=[int(r) for r in df3.iloc[ranking_dict[uni_to_plot], 1:]])],
    layout=go.Layout(
        xaxis=dict(range=[2019, 2022], autorange=True),
        title=f"{df3.iloc[ranking_dict[uni_to_plot], 0]} Historical Ranking"
    )
)
fig.update_layout(
xaxis = dict(
    tickmode = 'linear',
    tick0 = 2019,
    dtick = 1
),
    yaxis = dict(
    tickmode = 'linear',
    dtick = 1,
    autorange="reversed"
)
)

st.plotly_chart(fig)
