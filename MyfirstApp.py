import streamlit as st
import snowflake.connector as sncon

cnt1 = st.container()
cnt.header("Dashboard")

my_cnx = stc.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
mycur.execute("select state, country from COVID19_EPIDEMIOLOGICAL_DATA.PUBLIC.DEMOGRAPHICS")
