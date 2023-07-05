import streamlit as st
import snowflake.connector as sncon

con1 = sncon.connect(**st.secrets["snowflake"])
