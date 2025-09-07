import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go
import datetime

st.set_page_config(
     page_title="AdidasDashboard",
    layout="wide"
)
st.markdown('<style>div.body-container{padding-top:lrem;}</style>', unsafe_allow_html=True)
df = pd.read_excel(r"Adidas.xlsx")
image = Image.open("Logo.png")
col1,col2 =st.columns([0.1,0.9])
with col1:
    st.image(image,width = 100)
