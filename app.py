import streamlit as st
import pandas as pd

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
st.write('Historical Rankings')
df3 = df.copy()
df3 = df3.head(25)
df3 = df3[['Current Ranking', '2021 Ranking', '2020 Ranking', '2019 Ranking','University Name']]
df3 = df3[df3.columns[::-1]]

st.dataframe(df3)