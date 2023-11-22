import streamlit as st
import ui_components as ui

# Streamlit app
st.title("AXIS Cinfo")

# Main interface
st.button("Toggle On", on_click=ui.toggle_on)
st.button("Toggle Off", on_click=ui.toggle_off)
st.button("Algo_Test", on_click=ui.algo)
# st.button("Color", on_click=main("color"))
