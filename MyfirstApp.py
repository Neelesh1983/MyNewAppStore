import streamlit as st
import snowflake.connector as sncon

st.write(**st.secrets["snowflake"])
