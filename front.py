from urllib.request import urlopen
import json, streamlit as st

url1 = "http://127.0.0.1:8000/register_artikel/"
url2 = "http://127.0.0.1:8000/register_struktural/"
response1 = urlopen(url1)
data_json1 = json.loads(response1.read())
st.header("Data Artikel")
st.write(data_json1)

response2 = urlopen(url2)
data_json2 = json.loads(response2.read())
st.header("Data struktural")
st.write(data_json2)
