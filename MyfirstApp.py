import streamlit as st
import snowflake.connector as sncon

my_cnx = sncon.connect(
    user="Neelesh2023",
    password="Neelesh@2023",
    account="XN50895.ap-southeast-1.aws",
    database = "COVID19_EPIDEMIOLOGICAL_DATA",
     schema = "PUBLIC"
    )
my_cnx.cursor().execute("select top 100 state, county from DEMOGRAPHICS")
