import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go
import datetime
#st.write("hello world")
st.set_page_config(

    layout="wide"
)
st.markdown('<style>div.body-container{padding-top:lrem;}</style>', unsafe_allow_html=True)

st.write ("Hello Terra")

st.title("Streamlit Dashboard Example")

st.text("Streamlit is an open-source Python framework used to create interactive dashboards")
