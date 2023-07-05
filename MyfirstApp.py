import streamlit as st
import snowflake.connector as sncon

my_cnx = sncon.connect(**st.secrets["snowflake"])
