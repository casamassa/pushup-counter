import streamlit as st
import pandas as pd
from personal_ai import *

st.set_page_config(layout="wide")

personalAI = PersonalAI("video1.mp4")
personalAI.run()

placeholder = st.empty()
while True:
    frame, results, ts = personalAI.image_q.get()
    if ts == "done":
        break

    with placeholder.container():
        st.image(frame)