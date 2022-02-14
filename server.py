import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df: pd.DataFrame = pd.read_csv('run/log.txt', sep='\t')
df.columns = ['date', 'user']
df['date'] = pd.to_datetime(df['date']) + pd.Timedelta(hours=5, minutes=30)
df = df.set_index('date')

with st.container():
    st.title('Login result trend (7days)')
    cutoff_date = df.index[-1] - pd.Timedelta(days=7)
    cutoff_data = df[df.index > cutoff_date]

    # cutoff_data
    fig, ax= plt.subplots()

    ax.plot(pd.Series(cutoff_data.index), pd.Series(
        cutoff_data['user']), marker='.', linestyle=' ')

    st.pyplot(fig)

with st.container():
    st.title('Last 24 hours failure')
    cutoff_date = df.index[-1] - pd.Timedelta(days=1)
    cutoff_data = df[df.index > cutoff_date]

    failure_percentage = len(
        cutoff_data[cutoff_data['user'] == 'unknown'])/len(cutoff_data) * 100
    st.subheader(
        f'failed {round(failure_percentage, 2)}% out of {len(cutoff_data)} attempts')

with st.container():
    st.title('Last 7 days failure')
    cutoff_date = df.index[-1] - pd.Timedelta(days=7)
    cutoff_data = df[df.index > cutoff_date]

    failure_percentage = len(
        cutoff_data[cutoff_data['user'] == 'unknown'])/len(cutoff_data) * 100
    st.subheader(
        f'failed {round(failure_percentage, 2)}% out of {len(cutoff_data)} attempts')

with st.container():
    st.title('Last 30 days failure')
    cutoff_date = df.index[-1] - pd.Timedelta(days=30)
    cutoff_data = df[df.index > cutoff_date]

    failure_percentage = len(
        cutoff_data[cutoff_data['user'] == 'unknown'])/len(cutoff_data) * 100
    st.subheader(
        f'failed {round(failure_percentage, 2)}% out of {len(cutoff_data)} attempts')
