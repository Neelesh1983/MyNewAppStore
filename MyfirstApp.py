import streamlit as st
import snowflake.connector as sncon

cnt1 = st.container()
cnt.header("Dashboard")

my_cnx = sncon.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
mycur.execute("select top 100 state, county from DEMOGRAPHICS")
dr = mycur.fetchall()
df = st.dataframe(dr)
df
