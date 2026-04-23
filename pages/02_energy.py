import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Energy Efficiency", layout="wide")

st.title("⚡ Energy Efficiency & Sustainability")
st.info("Note: Efficiency metrics optimized for the tropical climate of Merida, Yucatan.")

# Interactive PUE Calculator
st.sidebar.header("PUE Calculator")
it_load = st.sidebar.number_input("IT Equipment Load (kW)", value=150.0)
cooling_load = st.sidebar.number_input("Cooling & Infrastructure Load (kW)", value=50.0)

total_load = it_load + cooling_load
pue = total_load / it_load

st.header(f"Current PUE: {pue:.2f}")

if pue <= 1.5:
    st.success("Efficient Operation (Tier III/IV Standard)")
else:
    st.warning("Efficiency improvement needed.")

# Chart: PUE Trends
st.subheader("Historical PUE Trends")

chart_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'PUE': [1.65, 1.60, 1.58, 1.52]
})

fig = px.line(
    chart_data, 
    x='Month', 
    y='PUE', 
    title='PUE Reduction 2026',
    markers=True
)

st.plotly_chart(fig, use_container_width=True)