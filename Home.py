import streamlit as st
import pandas as pd
import toml
from spacy.tokens import DocBin
from spacy_streamlit import visualize_spans
import glob
import spacy

st.title("Placing the Holocaust Annotations")

colors = toml.load("project.toml")

num=st.sidebar.selectbox("Select Testimony Number", [x for x in range(1, 41)])

if 'num' not in st.session_state:
    st.session_state["num"] = 1
st.session_state["num"] = num

with open(f"html/{st.session_state['num']:04}.html", "r") as f:
    html = f.read()

st.header(f"Testimony Number {num}")
st.markdown(html, unsafe_allow_html=True)